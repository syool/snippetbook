import numpy as np

from glob import glob
import os

path = '/home/user/Documents/VADSET/ped2/testing/frames'
gt_label = '/home/user/Documents/VADSET/ped2/frame_labels_ped2.npy'
labels = np.load(gt_label).squeeze()
window = 16

dict = {}
count = 0
for i, vid in enumerate(videos):
    frames = sorted(glob(os.path.join(vid, '*')))
        
    idx = f'{i+1}'
    n_frames = len(frames)
    l = labels[count:count+n_frames]
    dict[idx] = l
    
    count += n_frames

capsule = []
for i in range(len(dict)):
    idx = f'{i+1}'
    for e in range(len(dict[idx])):
        encap = dict[idx][e:e+window]
        
        if len(encap) < window:
            continue
        else:
            capsule.append(encap)
            
print(capsule)