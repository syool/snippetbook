import numpy as np
import torch
from PIL import Image

import os

os.chdir('/media/user/LinuxDrive/VAD_OpticalFlow/ped2/training/vis01')

vis = Image.open('./000000-vis.png')
vis = np.array(vis)
print(vis.shape)