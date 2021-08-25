import numpy as np

import os
os.chdir('/home/user/Downloads')


def softmax(x):
    c = np.max(x)
    y = np.exp(x-c)
    fx = y / np.sum(y)
    
    return fx


def softmax2d(x):
    dim = x.shape
    tmp = x.flatten()
    
    tmp = softmax(tmp)
    fx = tmp.reshape(dim)
    
    return fx


cquery = np.array([1, 2, 6, 3, 4])
tmp = softmax(cquery)

print(tmp)
print(tmp.cumsum()[-1])

#squery = np.random.randint(0, 10, (4, 3, 3))
squery = np.array([[[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[2, 1, 3],
                    [4, 6, 6],
                    [0, 8, 5]],
                   [[9, 1, 3],
                    [1, 7, 3],
                    [7, 6, 1]],
                   [[7, 4, 3],
                    [4, 7, 6],
                    [1, 0, 2]]])

attn = np.array([[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]])

res = softmax2d(squery[0])

print(res)
print(res.cumsum()[-1])