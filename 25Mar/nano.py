import torch
from model import Net  # 从 model.py 导入 Net 类
from PIL import Image
import torchvision.transforms as transforms
from PIL import ImageOps

# 加载模型
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = Net().to(device)
model.load_state_dict(torch.load('mnist_model.pth', map_location=device,weights_only=True  ))# 显式启用安全模式
    

model.eval()

# 预处理和预测函数
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
       # 调试输出，确认图像大小
    image = Image.open(image_path).convert('L')

    
    print(f"原始图像大小：{image.size}")
    # 颜色反转
    image_inverted = ImageOps.invert(image)
    image_inverted.show()  # 显示反转后的图片

    # 转换图像
    image = transform(image).unsqueeze(0).to(device)  # 添加 batch 维度

    # 检查图像 tensor 形状
    print(f"预处理后形状：{image.shape}")
    return image

def predict_digit(image_path):
    image = preprocess_image(image_path)
    with torch.no_grad():
        output = model(image)

        # 调试输出：查看原始模型输出
        print(f"模型原始输出：{output}")

        _, predicted = torch.max(output, 1)
        print(f"预测索引：{predicted.item()}")
              
    # 在 predict_digit 中添加
    print("概率明细：")
    for i, prob in enumerate(probabilities[0]):
               print(f"{i}: {prob.item():.4f}")

    return predicted.item()

# 预测你的手写数字
image_path = 'converted_image.png'  # 替换为你的图像路径
predicted_digit = predict_digit(image_path)
print(f'识别结果：{predicted_digit}')
