import cv2
import glob
import os
from tqdm import tqdm

main_dir = '/home/user/Downloads/AlphaRes'
dataset = 'ped2'
net_switch = '2d'
loss_switch = 'ssim'

target_dir = main_dir+'/'+dataset+'/{}-{}/errors'.format(net_switch, loss_switch)
log_dir = main_dir+'/'+dataset+'/{}-{}/heats'.format(net_switch, loss_switch)
os.makedirs(log_dir, exist_ok=True)

frames = glob.glob(os.path.join(target_dir, '*'))

for frame in tqdm(sorted(frames)):
    f = cv2.imread(frame, 0)
    heatmap = cv2.applyColorMap(f, cv2.COLORMAP_JET)
    
    name = frame.split('/')[-1]
    cv2.imwrite(log_dir+'/'+name, heatmap)