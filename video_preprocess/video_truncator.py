import torch
import numpy as np
import pickle

import cv2
import os
os.chdir('/home/user/Downloads/vidtest')


def truncate(video, FPS=24):
    '''
    ---
        video = str, name of the input video \n
        FPS = int, frame rate of the output (default=24)
    '''
    vid = cv2.VideoCapture(video)

    current_frame = 0
    
    cargo = []
    while(True):
        ret, frame = vid.read()
        
        if (ret is True) and (current_frame%FPS == 0):
            # cv2.imwrite('./data/img'+str(current_frame)+'.jpg', frame)
            
            arr = np.array(frame, dtype=np.float64)
            cargo.append(arr)
            # print(arr)
            # print(arr.shape)
            # np.save('./nparr/frame{}.npy'.format(current_frame), arr)
            
        elif ret is False:
            break
        
        current_frame += 1
    
    vid.release()
    # cv2.destroyAllWindows()
    
    return cargo

 
def save_pkl(cargo):
    with open('./container_002.pkl', 'wb') as container:
        for i in range(len(cargo)):
            pickle.dump(cargo[i], container, pickle.HIGHEST_PROTOCOL)
    
    print('{} frames are save into one pkl file.'.format(len(cargo)))
    container.close()


def read_pkl(pklfile):
    frames = []
    with open(pklfile, 'rb') as container:    
        while True:
            try: frames.append(pickle.load(container))
            except EOFError: break
            
        # for _ in range(len('?')):
        #     frames.append(pickle.load(container))
        
        # for statement is not working on it
        # since read_pkl() doesn't know the length of pklfile

    container.close()

    return frames



# frames = truncate('002.avi', FPS=5)
# save_pkl(frames)

l = read_pkl('./container_002.pkl')
print(l[0])
print(len(l))