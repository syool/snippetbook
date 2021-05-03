import scipy.io as sio
import numpy as np

import os
os.chdir('/home/user/Github/MNAD/data')

cargo = np.load('./frame_labels_shanghai.npy')
print(cargo.shape)
print(cargo)

# tmp = np.array([cargo])
# print(tmp)

# np.save('./frame_labels_shanghai.npy', tmp)