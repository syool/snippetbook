import numpy as np

from glob import glob
import pickle
import cv2

import os


def get_gtpixel(gt_path):
    gt = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)
    gt = cv2.resize(gt, dsize=(256, 256), interpolation=cv2.INTER_AREA)
    gt = gt[5:251, 5:251]
    gt = np.expand_dims(gt/255, axis=0)
    
    if len(np.unique(gt)) == 1: # all black
        return None, None
    else:
        in_gt = np.where(gt<=0.5, 0., 1.)
        out_gt = np.where(gt<0.5, 1., 0.)

        return in_gt, out_gt

def get_err(pkl_path):
    pkl = open(pkl_path, 'rb')
    err = pickle.load(pkl)
    
    return err

def inout_ratio(dataset, method, clip):
    gt_path = f'/home/user/Downloads/ratio/gt/{dataset}_gt'
    err_path = f'/home/user/Downloads/ratio/{method}_err/err_{dataset}.pkl'
    
    videos = sorted(glob(os.path.join(gt_path, '*')))
    errors = get_err(err_path)
    
    mu_list = []
    for gt_id, err_id in zip(videos, errors):
        gt_id = sorted(glob(os.path.join(gt_id, '*')))
        err_id = errors[str(err_id)]
        
        if len(gt_id[clip:]) == len(err_id):
            for gt, error in zip(gt_id[clip:], err_id):
                in_mask, out_mask = get_gtpixel(gt)
                
                if not (in_mask is None):
                    in_pixels = np.sum(in_mask)
                    out_pixels = in_mask.shape[0]*in_mask.shape[1]*in_mask.shape[2] - in_pixels
                    
                    in_err = in_mask * error
                    out_err = out_mask * error
                    
                    sum_in_err = np.sum(in_err)
                    sum_out_err = np.sum(out_err)
                    
                    numer = (1/out_pixels) * sum_out_err
                    demon = (1/in_pixels) * sum_in_err

                    mu = numer / demon
                    mu_list.append(mu)
                else:
                    continue
        else:
            print('ERROR: length of ground truth files and error files must be equal')
            
    return sum(mu_list)/len(mu_list)
    

method = 'final2'
clip = 20
val1 = inout_ratio(dataset='ped2', method=method, clip=clip)
val2 = inout_ratio(dataset='avenue', method=method, clip=clip)

print(f'ped2: {val1}, avenue: {val2}')

# memae clips = 15
# mnad, ammc = 4
# final2 = 20
