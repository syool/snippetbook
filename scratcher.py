import torch

import cv2
import numpy as np

import os

from torch.functional import Tensor

os.chdir('/home/user/Documents/AlphaRes/ped2/2d-ssim/heats')

a = cv2.imread('./error1.png', 0)
print(a)

a = torch.Tensor(a)
a = a.double()
a = torch.where(a<=25., 0., a)
a = Tensor.numpy(a)
cv2.imwrite('/home/user/Downloads/blah.png', a)

# a = cv2.imread('000008-vis.png', 0)
# a = torch.Tensor(a) # [0, 255] -> [0, 1]

# a = a.double()
# a = torch.where(a>=230., 250., a)
# a = Tensor.numpy(a)

# cv2.imwrite('/home/user/Downloads/a.png', a)

# a = torch.tensor([[1., 2., 3.],
#                   [4., 5., 6.]])

# a = a.double()
# a = torch.where(a>=4., 0., a)
# print(a)

