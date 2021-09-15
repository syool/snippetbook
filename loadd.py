import numpy as np

from glob import glob
from collections import OrderedDict

import os

path = '/home/user/Documents/VADSET'
dataset = 'shanghai'
valid = 'training' # 'training' or 'testing'

lane = path+'/'+dataset+'/'+valid+'/frames'

videos = sorted(glob(os.path.join(lane, '*')))

def get_samples():
    entry = []
    for vid in videos:
        fr = sorted(glob(os.path.join(vid, '*')))
        for i in fr:
            entry.append(i)
            
    return entry
        
def __len__():
    return len(get_samples())

a = get_samples()
print(a[1])