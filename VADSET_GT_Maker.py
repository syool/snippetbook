import numpy as np

import scipy.io as sio
import numpy as np

from glob import glob
import os

dataset = 'ped2'
root = f'/home/user/Documents/GT/{dataset}_gt'
videos = sorted(glob(os.path.join(root, '*')))

print(f'working on {dataset}...')

gtl = []
for i, vid in enumerate(videos):
    idx = f'{i+1}'.zfill(3)
    r = sio.loadmat(vid)
    gtl += list(r['l'][0])
    
    print(vid, len(r['l'][0]))

np.save(f'/home/user/Downloads/{dataset}_gt.npy', gtl)
print(len(gtl), 'labels saved')