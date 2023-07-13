import torchvision.transforms as transforms
from PIL import Image

import torch
import torchvision.models as models

# 检查CUDA是否可用并选择设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载DeepLabv3模型
model = models.segmentation.deeplabv3_resnet101(pretrained=True)

model.to(device)
model.eval()

# 图像预处理
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(
        mean=torch.tensor([0.485, 0.456, 0.406]).to(device),
        std=torch.tensor([0.229, 0.224, 0.225]).to(device)
    )
])

# 加载输入图像
image = Image.open('D2D38886136FCD3C1FDF73CB0FA0235F.png')


# 图像预处理
input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)
input_batch = input_batch.to(device)

# 将输入数据传递给模型进行预测
with torch.no_grad():
    output = model(input_batch)['out'][0]
output_predictions = output.argmax(0)

# 将预测结果转换为掩码图像
mask = output_predictions.byte().cpu().numpy()
mask_image = Image.fromarray(mask * 255).resize(image.size)

# 创建一个与输入图像相同大小的空白图像，并将掩码应用于空白图像
result = Image.new('RGBA', image.size)
result.paste(image, (0, 0), mask_image)

# 保存结果图像
result.save('accu2_2out00001.png')