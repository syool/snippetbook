import numpy as np
from PIL import Image


# img = Image.open("NASA.jpg")
# imgArray = np.asarray(img)
# print(imgArray.shape)

path = '/home/user/Documents/AlphaRes/ped2/2d-perce/log_pretask/errors'
img = Image.open(path+'/error1.png')
img = np.asarray(img)
print(img)