import torch

import numpy as np
from PIL import Image

import os

from torchvision import transforms
import torchvision.utils as vutils
os.chdir('/home/user/Downloads')

t1 = transforms.ToTensor()
t2 = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])

fake = Image.open('./eee/2dssim.png')
fake = t1(fake)
fake = t2(fake)

real = Image.open('./eee/real.png')
real = t1(real)
real = t2(real)

a = torch.subtract(real, fake)
print(a)
# vutils.save_image(a, './eee/residual.png')