import torch
import numpy as np
import pickle
from tqdm import tqdm

import cv2
import os
os.chdir('/home/user/Downloads/')


def _mkdir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print ('Error: Creating directory of data')


def run(path, videos, opt, fill, extension='.jpg'):
    print('current location:', loc)
    print('video list:', videos)
    
    if opt=='A': # option A: save all frames into one foloder
        
        target_path = './frames/'
        _mkdir(target_path)
        
        # indexing over double loop.
        # here, index in the while statement is counted cummulatively
        # over the for statement.
        
        index = [0] # it remembers the last counting at each end of the while statement
        
        for i in tqdm(range(len(videos))):
            vid = cv2.VideoCapture(loc+videos[i])
        
            while True:
                ret, frame = vid.read()
                
                if ret is True:
                    i = index[-1] # fetch the last counting from the previous while loop
                    i += 1
                    index.append(i)
                    
                    name = target_path + str(i).zfill(fill)+extension # 0000n.jpg
                    cv2.imwrite(name, frame)
                
                elif ret is False:
                    break
            
            vid.release()
    
    elif opt=='B': # option B: save frames into each folder
        
        for i in tqdm(range(len(videos))):
            tmp = os.path.splitext(videos[i])[0] # remove file extension
            
            target_path = './frames/{}/'.format(tmp)
            _mkdir(target_path)
            
            vid = cv2.VideoCapture(loc+videos[i])
            
            i = 1
        
            while True:
                ret, frame = vid.read()
                        
                if ret is True:
                    name = target_path + str(i).zfill(fill)+extension # 0000n.jpg
                    cv2.imwrite(name, frame)
                            
                    i += 1
                            
                elif ret is False:
                    break
            
            vid.release()


loc = '/home/user/Downloads/sh_training/'
videos = sorted(os.listdir(loc))

run(loc, videos, opt='B', fill=3)