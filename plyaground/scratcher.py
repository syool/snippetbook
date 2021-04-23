import scipy.io as sio
import numpy as np

import os

# path = '/home/user/Github/memae-anomaly-detection/datasets/processed/CUHKAvenue/Test_gt'

# os.chdir(path)
# filelist = sorted(os.listdir(path))
# print(filelist)

# for i in range(len(filelist)):
#     e = sio.loadmat(filelist[i])['l'][0]
#     print(filelist[i])
#     print(e.shape)
#     print(e)


# path = '/home/user/Downloads/AD_datasets/shanghaitech/testing/Test_gt_npy'

# os.chdir(path)
# filelist = sorted(os.listdir(path))
# print(filelist)

# for i in range(len(filelist)):
#     cargo = np.load(filelist[i])
#     print(filelist[i])
#     print(cargo.shape)
#     print(cargo)


# path = '/home/user/Github/MNAD/data'
# os.chdir(path)

# files = sorted(os.listdir(path))
# print(files, '\n')

# for i in range(1, len(files)):
#     cargo = np.load(files[i])
#     print(files[i])
#     print(cargo)
#     print(cargo.shape)
#     print()


path = '/home/user/Github/MNAD/dataset/ped2/training/'
os.chdir(path)

files = sorted(os.listdir(path))
print(files, '\n')

for i in range(len(files)):
    base = os.path.splitext(files[i])[0]
    os.rename(files[i], base+'.jpg')