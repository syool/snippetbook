# convert pixel level ground truth .mat to frame level gt .mat

import scipy.io as sio
import numpy as np

import os

path = '/home/user/Downloads/AD_datasets/shanghaitech/testing/Test_gt/'

os.chdir(path)
filelist = sorted(os.listdir(path))
print(filelist)


for i in range(len(filelist)):
    cargo = sio.loadmat(filelist[i])['volLabel'][0]

    code = []
    for j in range(len(cargo)):
        if np.max(cargo[j]) != 0: code.append(1)
        else: code.append(0)

    code = np.array(code, dtype='uint8')
        
    print(code)
    print(len(code))

    dict = {
        'l': code
    }

    sio.savemat('new{}.mat'.format(i), dict)

# ee = sio.loadmat('new.mat')
# print(ee)

# bb = sio.loadmat('/home/user/Github/memae-anomaly-detection/datasets/processed/UCSD_P2_256/Test_gt/Test001.mat')
# print(bb)