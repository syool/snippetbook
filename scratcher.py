import torch

import cv2
import numpy as np
from glob import glob

import os

from torch.functional import Tensor

path = '/home/user/Documents/AlphaRes/ped2/2d-ssim-l1/errors'
frames = sorted(glob(os.path.join(path, '*')))

for frame in frames:
    a = cv2.imread(frame, 0)

    a = torch.Tensor(a)
    a = a.double()
    a = torch.where(a<=30., 0., a+30.)
    a = Tensor.numpy(a)
    
    name = frame.splt('/')[-1]
    cv2.imwrite('/home/user/Downloads/re/{}'.format(name), a)

a = cv2.imread('000008-vis.png', 0)
a = torch.Tensor(a) # [0, 255] -> [0, 1]

a = a.double()
a = torch.where(a>=230., 250., a)
a = Tensor.numpy(a)

cv2.imwrite('/home/user/Downloads/a.png', a)
