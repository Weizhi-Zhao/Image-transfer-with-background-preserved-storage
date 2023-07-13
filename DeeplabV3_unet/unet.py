import torch
import torchvision.transforms as transforms
from PIL import Image
import torchvision.models as models
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# 加载预训练的DeepLabv3模型
model = models.segmentation.deeplabv3_resnet101(pretrained=True)

# 设置模型为评估模式
model.eval()

# 加载输入图像并进行预处理
input_image = Image.open('D2D38886136FCD3C1FDF73CB0FA0235F.png')
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
input_tensor = preprocess(input_image).unsqueeze(0)

# 将输入数据传递给模型进行预测
with torch.no_grad():
    output = model(input_tensor)['out'][0]

# 将输出结果转换为二值图像
output = output.argmax(0).byte()

# 将二值图像转换为灰度图像
output_image = transforms.ToPILImage()(output)

# 显示和保存结果图像
output_image.show()
output_image.save('output_image.png')

