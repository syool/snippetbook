import torch
import torch.nn.functional as F

import numpy as np
import os


def weave(num_weave, patch_a, patch_b, dim):
    x = []
    for i in range(num_weave):
        if i % 2 == 0: x.append(patch_a)
        else: x.append(patch_b)
    
    x = torch.cat(x, dim=dim)
    
    return x

def cubic_mask(cube_size, weave_size):
    r'''
    parameters:
    -----------
        cube_size (list): [C, H, W]
        weave_size (list): [C, H, W]
    '''
    cube0 = torch.zeros([cube_size[0], cube_size[1], cube_size[2]])
    cube1 = torch.ones([cube_size[0], cube_size[1], cube_size[2]])

    row0 = weave(weave_size[1], cube0, cube1, dim=2)
    row1 = weave(weave_size[1], cube1, cube0, dim=2)

    frame0 = weave(weave_size[2], row0, row1, dim=1)
    frame1 = weave(weave_size[2], row1, row0, dim=1)
    
    mask0 = weave(weave_size[0], frame0, frame1, dim=0)
    mask1 = weave(weave_size[0], frame1, frame0, dim=0)
    
    return mask0, mask1
    
zero_start, one_start = cubic_mask([4, 32, 32], [4, 8, 8])
print(torch.unsqueeze(zero_start, dim=0).shape) # 4 dimensional
print(one_start.shape)