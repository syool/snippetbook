import torch
import torchvision.transforms as transforms

import numpy as np
from PIL import Image

# canvas = Image.new('RGB', (256, 256), (0, 0, 0))
# print(canvas)

# tr = transforms.Compose([
#         transforms.Grayscale(),
#         transforms.ToTensor(),
#         transforms.Normalize(([0.5]), ([0.5])),
#         # ToTensor: [0, 255] -> [0, 1]
#         # Normalize: [0, 1] -> [-1, 1]
#     ])

# canvas = tr(canvas)
# print(canvas)

canvas = torch.full((1, 256, 256), -1.)
print(canvas)