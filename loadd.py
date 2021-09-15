import numpy as np

from glob import glob
from collections import OrderedDict

import os

path = '/home/user/Documents/VADSET'
dataset = 'ped2'
valid = 'training' # 'training' or 'testing'

lane = path+'/'+dataset+'/'+valid+'/frames'

videos = sorted(glob(os.path.join(lane, '*')))
frames = OrderedDict()
idx_list = []

def get_samples():
    for vid in videos:
        idx = vid.split('/')[-1]
        idx_list.append(idx)
        x = sorted(glob(os.path.join(vid, '*.jpg')))
        frames[idx] = x

