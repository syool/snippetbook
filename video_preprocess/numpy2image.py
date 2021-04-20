import numpy as np
from PIL import Image

import os

try:
    if not os.path.exists('/home/user/Downloads/GT_Shanghai/'):
        os.makedirs('/home/user/Downloads/GT_Shanghai/')
except OSError:
    print ('Error: Creating directory of data')

os.chdir('/home/user/Downloads/GT_Shanghai/')



path = '/home/user/Downloads/AD_datasets/shanghaitech/testing/test_pixel_mask/'
filename = sorted(os.listdir(path)) # fetch file names by order
print(len(filename), 'files are fetched')


cargo = np.load(path+filename[0])
print(filename[0])
print(cargo.shape)
print(cargo[0].shape)
print(cargo[0])


for i in range(len(filename)):
    print('read: ', path+filename[i])
    cargo = np.load(path+filename[i])
    
    print('video {}'.format(i+1), cargo.shape)
    gtruth = np.where(cargo==1, 255, cargo) # change value 1 to 255 (white)
    
    name = os.path.splitext(filename[i])[0] # getting rid of file extension from filenames

    try:
        if not os.path.exists(name):
            os.makedirs(name)
    except OSError:
        print ('Error: Creating directory of data')

    for j in range(len(gtruth)):
        image = Image.fromarray(gtruth[j], '1')
        image.save('./'+name+'/'+str(j+1).zfill(3)+'.bmp')
        
print('DONE')