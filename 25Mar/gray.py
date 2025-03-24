from PIL import Image
import torchvision.transforms as transforms

# 图像路径
image_path = 'your_image.png'  # 替换成你的图片路径
output_path = 'converted_image.png'  # 转换后的图片保存路径

# 定义转换流程
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # 转为灰度
    transforms.Resize((28, 28))                   # 调整为 28x28
])

# 加载原始图像
image = Image.open(image_path)

# 转换图像
gray_image = transform(image)

# 保存转换后的图像
gray_image.save(output_path)

# 显示转换后的图像
gray_image.show()

print(f"灰度图已保存至：{output_path}")
