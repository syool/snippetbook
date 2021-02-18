import os, sys
os.chdir('/home/user/Downloads/ava_v2.1')

''' AVA Action Dataset '''
''' Get urls: https://github.com/cvdfoundation/ava-dataset '''
''' Get annotations: http://research.google.com/ava/index.html '''

import time
from tqdm import tqdm
from urllib import request

codec = 'utf-8'
switch = 'train' # train or test
head_train = 'https://s3.amazonaws.com/ava-dataset/trainval/'
head_test = 'https://s3.amazonaws.com/ava-dataset/test/'

def fetch(head, switch=switch):
    os.makedirs('./videos/{}'.format(switch), exist_ok=True)
    
    if switch == 'train': txtfile = 'ava_file_names_trainval_v2.1.txt'
    elif switch == 'test': txtfile = 'ava_file_names_test_v2.1.txt'
        
    tails = []
    with open(txtfile, 'rt', encoding=codec) as input: 
        for tail in input: # read sentence by sentence
            tail = tail.rstrip()
            tails.append(tail)
            
        for i in tqdm(range(len(tails))):
            try:
                request.urlretrieve(head+tails[i], './videos/{}/{}'.format(switch, tails[i]))
            except: continue # ingore errors and keep looping
            
    input.close()
    
fetch(head_train, switch='train')
print('downloading trainval done')

fetch(head_test, switch='test')
print('downloading test done')