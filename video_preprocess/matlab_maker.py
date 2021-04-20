# create .mat from numpy

import scipy.io as sio
import numpy as np

import os

path = '/home/user/Downloads/AD_datasets/shanghaitech/testing/Test_gt_npy/'
save_path = '/home/user/Downloads/AD_datasets/shanghaitech/testing/Test_gt_mat/'

os.chdir(path)
filelist = sorted(os.listdir(path))
print(filelist)

try:
    if not os.path.exists(save_path):
        os.makedirs(save_path)
except OSError:
    print ('Error: Creating directory of data')

for i in range(len(filelist)):
    cargo = np.load(filelist[i])

    # print(cargo)
    # print(len(cargo))
    # print()

    code = np.array(cargo, dtype='uint8')
    
    dict = {
        'l': code
    }
    
    sio.savemat(save_path+'new{}.mat'.format(i), dict)
    
    ee = sio.loadmat(save_path+'new{}.mat'.format(i))
    print(ee)