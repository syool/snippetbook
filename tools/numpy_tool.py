import numpy as np
from PIL import Image

import os
os.chdir('/home/user/Downloads/GT_Shanghai/')

path = '/home/user/Downloads/AD_datasets/shanghaitech/testing/test_pixel_mask/'
filename = os.listdir(path)
print(len(filename))

for i in range(len(filename)):
    print('read: ', path+filename[i])
    cargo = np.load(path+filename[i])
    
    name = os.path.splitext(filename[i])[0] # getting rid of file extension from filenames

    try:
        # creating a folder named data
        if not os.path.exists(name):
            os.makedirs(name)
    
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')

    for j in range(len(cargo)):
        image = Image.fromarray(cargo[j], '1')
        image.save('./'+name+'/'+str(j+1).zfill(3)+'.bmp')
        
print('DONE')