import torch
import numpy as np
import pickle

import cv2
import os
os.chdir('/home/user/Downloads/')


def truncate(video, opt, loop, FPS=24):
    '''
    ---
        video = str, name of the input video \n
        FPS = int, frame rate of the output (default=24)
    '''
    vid = cv2.VideoCapture(video)
    path = './SH_train/'+str(loop).zfill(3)

    current_frame = 1
    
    try:
        # creating a folder named data
        if not os.path.exists(path):
            os.makedirs(path)
  
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    
    if opt == 'frame':
        while True:
            ret, frame = vid.read()
            
            if (ret is True):
                name = path+'/'+str(current_frame).zfill(3)+'.tif'
                cv2.imwrite(name, frame)
                
                current_frame += 1
                
            elif ret is False:
                break
            
        vid.release()
        # cv2.destroyAllWindows()
    
    elif opt == 'pkl':
        cargo = []
        while True:
            ret, frame = vid.read()
            
            if (ret is True) and (current_frame%FPS == 0):
                arr = np.array(frame, dtype=np.float64)
                cargo.append(arr)
                # print(arr)
                # print(arr.shape)
                # np.save('./nparr/frame{}.npy'.format(current_frame), arr)
                
                current_frame += 1
                
            elif ret is False:
                break
    
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



data_path = '/home/user/Downloads/AD_datasets/shanghaitech/training/videos_rename/'

for i in range(1, 331):
    frames = truncate(data_path+str(i).zfill(3)+'.avi', opt='frame', loop=i, FPS=24)
    print('video {} done'.format(i))

print()
print('TERMINATE')

# save_pkl(frames)

# l = read_pkl('./container_002.pkl')
# print(l[0])
# print(len(l))