import torch
from model import Net
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt  # 调试可视化

# 加载模型
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = Net().to(device)

# 安全加载模型权重
try:
    model.load_state_dict(
        torch.load(
            'mnist_model.pth', 
            map_location=device
        )
    )
    print("✅ 模型权重加载成功")
except Exception as e:
    print(f"❌ 加载失败: {str(e)}")
    exit()

model.eval()

# 预处理函数
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),
        transforms.Lambda(lambda x: 1 - x)  # 颜色反转（重要！）
    ])
    
    # 加载图像，转换为灰度
    image = Image.open(image_path).convert('L')
    print(f"🖼️ 原始图像大小：{image.size}")
    
    # 可视化原始图像
    plt.imshow(image, cmap='gray')
    plt.title("Original Image (Before Processing)")
    plt.show()
    
    # 进行预处理
    image_tensor = transform(image)
    
    # 打印预处理后图像信息
    print(f"📊 预处理后张量形状：{image_tensor.shape}")
    print(f"🔍 张量像素范围 (min, max)：{image_tensor.min().item()}, {image_tensor.max().item()}")
    
    # 反转颜色后的图像
    inverted_image = 1 - image_tensor
    plt.imshow(inverted_image.squeeze(0), cmap='gray')
    plt.title("Inverted Image (After Color Inversion)")
    plt.show()
    
    # 添加 batch 维度
    image_tensor = image_tensor.unsqueeze(0).to(device)
    return image_tensor

# 预测函数
def predict_digit(image_path):
    image = preprocess_image(image_path)
    
    with torch.no_grad():
        # 模型推理
        output = model(image)
        
        # 计算概率分布
        probabilities = torch.nn.functional.softmax(output, dim=1)
        print(f"📈 各数字概率分布：{probabilities.cpu().numpy()[0]}")
        
        # 可视化概率分布
        plt.bar(range(10), probabilities.cpu().numpy()[0])
        plt.title("Prediction Probability Distribution")
        plt.xlabel("Digit Class")
        plt.ylabel("Probability")
        plt.show()
        
        # 获取最大概率的类别
        _, predicted = torch.max(output, 1)
    
    print(f"🎯 识别结果：{predicted.item()}")
    return predicted.item()

# 测试
image_path = 'converted_image (5).png'
predicted_digit = predict_digit(image_path)
print(f'最终识别结果：{predicted_digit}')
