import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        # 1. 拉平：把 (batch, 28, 28) 变成 (batch, 784)
        x = x.view(x.size(0), -1)
        
        # 2. 第一层 + 激活
        x = self.fc1(x)
        x = self.relu(x)
        
        # 3. 输出层（不加 Softmax）
        x = self.fc2(x)
        return x
    
