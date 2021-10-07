import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models

# path = '/home/user/Documents/VADSET'
# dataset = 'ped2'
# gt_label = '{}/frame_labels_{}.npy'.format(path, dataset)

# label = np.load(gt_label)

# li = label.squeeze()
# print(li)

# torch.manual_seed(0)

# a = torch.rand([8, 512, 4, 4])
# batch, C, H, W = a.shape

# a = a.permute(0, 2, 3, 1)
# x = a.contiguous().view(-1, C)
# y = a.contiguous().view(batch*H*W, C)

# print(x)
# print(y)

net = models.vgg16().features
module = nn.Sequential()

for i in range(16):
    module.add_module(str(i), net[i])
    
for params in module.parameters():
    params.requires_grad = False
    
print(module)