from __future__ import division

import numpy as np
import torch
import torch.nn as nn
from PIL import Image
from torchvision import models
from torchvision import transforms

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)


def load_image(image_path, transform=None, max_size=None, shape=None):
    image = Image.open(image_path)
    if max_size:
        scale = max_size / max(image.size)
        size = np.array(image.size) * scale
        image = image.resize(size.astype(int), Image.ANTIALIAS)

    if shape:
        image = image.resize(shape, Image.LANCZOS)

    if transform:
        image = transform(image).unsqueeze(0)

    return image.to(device)


transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

content = load_image("C:/Users/qwe/Desktop/content666.jpg", transform, max_size=700)
style = load_image("C:/Users/qwe/Desktop/style.jpg", transform, shape=[content.size(2), content.size(3)])


class VGGNet(nn.Module):
    def __init__(self):
        super(VGGNet, self).__init__()
        self.select = ['0', '5', '10', '19', '28']
        self.vgg = models.vgg19(pretrained=True).features

    def forward(self, x):
        features = []
        for name, layer in self.vgg._modules.items():
            x = layer(x)
            if name in self.select:
                features.append(x)
        return features


target = content.clone().requires_grad_(True)
optimizer = torch.optim.Adam([target], lr=0.11, betas=[0.5, 0.999])
vgg = VGGNet().to(device).eval()
target_features = vgg(target)
total_step = 10
style_weight = 400.
for step in range(total_step):
    target_features = vgg(target)
    content_features = vgg(content)
    style_features = vgg(style)
    style_loss = 0
    content_loss = 0
    for f1, f2, f3 in zip(target_features, content_features, style_features):
        content_loss += torch.mean((f1 - f2) ** 2)
        _, c, h, w = f1.size()
        f1 = f1.view(c, h * w)
        f3 = f3.view(c, h * w)

        # 计算gram matrix
        f1 = torch.mm(f1, f1.t())
        f3 = torch.mm(f3, f3.t())
        style_loss += torch.mean((f1 - f3) ** 2) / (c * h * w)

    loss = content_loss + style_weight * style_loss

    # 更新target
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if step % 10 == 0:
        print("Step [{}/{}], Content Loss: {:.4f}, Style Loss: {:.4f}"
              .format(step, total_step, content_loss.item(), style_loss.item()))

denormalize = transforms.Compose([transforms.Normalize(mean=[-0.485 / 0.229, -0.456 / 0.224, -0.406 / 0.225],
                                                       std=[1 / 0.229, 1 / 0.224, 1 / 0.225])])
img = denormalize(target.clone()).squeeze().cpu().detach().clamp_(0, 1)
img_pil = transforms.ToPILImage()(img)
img_pil.save("output_image.jpg")
