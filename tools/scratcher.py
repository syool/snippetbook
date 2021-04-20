import scipy.io as sio
import numpy as np

import os

path = '/home/user/Github/memae-anomaly-detection/datasets/processed/CUHKAvenue/Test_gt'

os.chdir(path)
filelist = sorted(os.listdir(path))
print(filelist)

for i in range(len(filelist)):
    e = sio.loadmat(filelist[i])['l'][0]
    print(filelist[i])
    print(e.shape)
    print(e)


# path = '/home/user/Downloads/AD_datasets/shanghaitech/testing/Test_gt_npy'

# os.chdir(path)
# filelist = sorted(os.listdir(path))
# print(filelist)

# for i in range(len(filelist)):
#     cargo = np.load(filelist[i])
#     print(filelist[i])
#     print(cargo.shape)
#     print(cargo)