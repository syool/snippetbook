import torch

import cv2
import numpy as np

import os

from torch._C import dtype

os.chdir('/media/user/LinuxDrive/VAD_OpticalFlow/ped2/testing/vis01')

# a = cv2.imread('000008-vis.png', 0)
# a = torch.Tensor(a)
# a = torch.flatten(a)
# a = [0 if i >= 230 else i for i in a]
# print(a.shape)

a = torch.tensor([[1., 2., 3.],
                  [4., 5., 6.]])

a = a.double()
a = torch.where(a>=4., 0., a)
print(a)

