import torch
from model import Net
from torchvision import datasets, transforms

# 设置设备
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# 重新实例化模型
model = Net().to(device)

# 加载模型权重
model.load_state_dict(torch.load('mnist_model.pth', map_location=device))
model.eval()  # 设置为评估模式
print("✅ 模型加载成功，正在进行验证...")

# 加载测试数据集
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 下载并加载 MNIST 测试集
test_dataset = datasets.MNIST('data/', train=False, download=True, transform=transform)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)

# 计算准确率
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images.view(-1, 28 * 28))  # 展平图片
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f"🎯 测试集准确率：{accuracy:.2f}%")


# 加载模型权重
state_dict = torch.load('mnist_model.pth')

# 查看权重键值
print(state_dict.keys())
