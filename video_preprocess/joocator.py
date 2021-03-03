import cv2
import os
from time import time

os.chdir('/home/user/Downloads')

def extract_multiple_videos(input_lists):
    for input_list in input_lists:

        input_filenames = os.listdir('./UCF-101/'+input_list)
        #input_filenames = os.listdir('mp4/' + input_list)
        i = 0

        for input_filename in input_filenames:
            cam = cv2.VideoCapture('./UCF-101/'+input_list +'/'+ input_filename)
            #cam = cv2.VideoCapture('mp4/' + input_list + '/' + input_filename)
            i = i + 1

            try:

                # creating a folder named data
                if not os.path.exists('./UCF-101/demo/'+input_list+'/'+input_list + str(i)):
                    os.makedirs('./UCF-101/demo/'+input_list+'/'+input_list + str(i))
                  #if not os.path.exists('data/'+input_list + str(i)):
                   #  os.makedirs('data/'+input_list + str(i))

                    # if not created then raise error
            except OSError:
                print('Error: Creating directory of data')

                # frame
            currentframe = 0
            #prev_time = 0
            while (True):
                ret, frame = cam.read()
                #current_time = time() - prev_time
                #print(ret)
                if (ret is True) and (currentframe%5 == 0):
                    # if video is still left continue creating images
                    name = './UCF-101/demo/'+input_list+'/'+input_list + str(i) + '/img_' + str(currentframe) + '.jpg'
                    #name = './data/'+input_list + str(i) + '/img_' + str(currentframe) + '.jpg'

                    print('Creating...' + name)

                    # writing the extracted images
                    cv2.imwrite(name, frame)
                    #prev_time = time()

                if (ret is False):
                    break

                    # increasing counter so that it will
                    # show how many frames are created
                currentframe += 1
            # Release all space and windows once done
            cam.release()
            cv2.destroyAllWindows()

if __name__ == '__main__':
    #input_filenames=['UCF-101/Biking/v_Biking_g01_c04.avi','UCF-101/Skiing/v_Skiing_g01_c01.avi']

    #file_list=os.listdir('UCF-101/Biking')
    #print(file_list)
    #extract_multiple_videos(file_list)

    file_list=os.listdir('./UCF-101')
    print(file_list[0:1])
    extract_multiple_videos(file_list[0:3])

    #file_list=os.listdir('mp4')
    #extract_multiple_videos(file_list)
