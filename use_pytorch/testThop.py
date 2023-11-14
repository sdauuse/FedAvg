# author: miaoyin
# time: 2023-11-13 12:24
from thop import profile
from thop import clever_format
from torchsummary import summary
import torch
import Models

# ------------------训练一轮模型FLOPs和参数----------------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
net = Models.Mnist_CNN().to(device)
input_shape = (3, 224, 224)
summary(net, input_shape)

input_tensor = torch.randn(1, *input_shape).to(device)
macs, params = profile(net, inputs=(input_tensor,))
# flops ≈ macs*2
flops, params = clever_format([macs * 2, params], "%.3f")
print("FLOPs: ", flops)
print("params: ", params)
print("\n分割线###########################################")
# ------------------设置训练n轮，训练n轮模型FLOPs和参数----------------------
# 例如训练100轮
n = 100
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
net = Models.Mnist_CNN().to(device)
input_shape = (3, 224, 224)
summary(net, input_shape)

input_tensor = torch.randn(1, *input_shape).to(device)
macs, params = profile(net, inputs=(input_tensor,))
# flops ≈ macs*2
flops, params = clever_format([n * macs * 2, n * params], "%.3f")
print("FLOPs: ", flops)
print("params: ", params)
