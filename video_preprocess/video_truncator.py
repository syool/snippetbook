import cv2
import numpy as np

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
    
    while(True):
        ret, frame = vid.read()
        
        if (ret is True) and (current_frame%FPS == 0):
            cv2.imwrite('./data/img'+str(current_frame)+'.jpg', frame)
            
        elif ret is False:
            break
        
        current_frame += 1
        print(current_frame)

    vid.release()
    # cv2.destroyAllWindows()



truncate('001.mp4', FPS=50)