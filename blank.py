import numpy as np
import torch
import torch.nn.functional as F

# path = '/home/user/Documents/VADSET'
# dataset = 'ped2'
# gt_label = '{}/frame_labels_{}.npy'.format(path, dataset)

# label = np.load(gt_label)

# li = label.squeeze()
# for i in range(len(li)):
#     print(i, li[i])


a = ([3, 2, 1])

t = a.max(1)
print(t)