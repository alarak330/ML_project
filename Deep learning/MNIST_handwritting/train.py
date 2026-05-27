from model import NeuralNet

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt



BATCH_SIZE = 64
LEARNING_RATE = 0.001
EPOCHS = 10
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.ToTensor(),                          # 把PIL图片转成Tensor，顺便除以255
    transforms.Normalize((0.1307,), (0.3081,))      # MNIST的经验均值和标准差
])

# 下载并加载训练集和测试集
train_dataset = datasets.MNIST(
    root="./data",        # 数据存放路径
    train=True,           # 训练集
    transform=transform,  # 应用上面的预处理
    download=True         # 没下载过就自动下载
)

test_dataset = datasets.MNIST(
    root="./data",
    train=False,          # 测试集
    transform=transform,
    download=True
)

# 用 DataLoader 批量加载
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader  = DataLoader(test_dataset,  batch_size=BATCH_SIZE, shuffle=False)

model = NeuralNet().to(DEVICE)                      # 实例化并移到设备
criterion = nn.CrossEntropyLoss()                   # 多分类交叉熵（自带Softmax）
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)  # Adam优化器

def train():
    model.train()  # 训练模式
    for epoch in range(EPOCHS):
        total_loss = 0
        for images, labels in train_loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            
            # 前向传播
            outputs = model(images)
            loss = criterion(outputs, labels)
            
            # 反向传播三部曲
            optimizer.zero_grad()   # 清空旧梯度
            loss.backward()         # 计算新梯度
            optimizer.step()        # 更新参数
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_loader)
        print(f"Epoch [{epoch+1}/{EPOCHS}], Loss: {avg_loss:.4f}")
def test():
    model.eval()  # 评估模式
    correct = 0
    total = 0
    with torch.no_grad():  # 不计算梯度，省显存+加速
        for images, labels in test_loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)  # 取10个输出中最大的那个
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = 100.0 * correct / total
    print(f"Test Accuracy: {accuracy:.2f}%")

def visualize_predictions(num_images=6):
    model.eval()
    images, labels = next(iter(test_loader))
    images, labels = images[:num_images].to(DEVICE), labels[:num_images]
    
    with torch.no_grad():
        outputs = model(images)
        _, preds = torch.max(outputs, 1)
    
    fig, axes = plt.subplots(1, num_images, figsize=(12, 4))
    for i in range(num_images):
        img = images[i].cpu().squeeze()
        axes[i].imshow(img, cmap="gray")
        axes[i].set_title(f"Pred: {preds[i].item()}\nTrue: {labels[i].item()}")
        axes[i].axis("off")
    plt.show()
    
if __name__ == "__main__":
    train()
    test()
    visualize_predictions()