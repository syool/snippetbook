import cv2
from time import time

import os
os.chdir('/home/user/Downloads/vidtest')


def truncate(video, FPS):
    '''
    ---
        video = str, name of the input video \n
        FPS = int, frame rate of the output 
    '''
    vid = cv2.VideoCapture(video)

    i = 0
    prev_time = 0

    while(vid.isOpened()):
        ret, frame = vid.read()
        
        current_time = time() - prev_time
        
        if (ret is True) and (current_time > 1./FPS):
            # cv2.imwrite('./data/img'+str(i)+'.jpg', frame)
            print(frame)
            prev_time = time()
            
            if cv2.waitKey(1) > 0:
                break
        
        i += 1
        
    vid.release()
    cv2.destroyAllWindows()



truncate('001.mp4', FPS=50)