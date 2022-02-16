import numpy as np

from typing import Tuple, Union
import cv2


def get_gtmask(gt_path: str, resize: bool = False) -> Tuple[np.array, np.array]:
    gt = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)
    
    if resize:
        gt = cv2.resize(gt, dsize=(256, 256), interpolation=cv2.INTER_AREA)
        gt = gt[5:251, 5:251]/255
        # gt = np.expand_dims(gt/255, axis=0)
    
    if len(np.unique(gt)) == 1: # all black
        return None, None
    else:
        in_mask = np.where(gt<=0.5, 0., 1.)
        out_mask = np.where(gt<0.5, 1., 0.)

        return in_mask, out_mask


def get_error(err_path: str, normalize: bool = True) -> np.array:
    err = cv2.imread(err_path, cv2.IMREAD_GRAYSCALE)
    if normalize:
        err = (err - err.min()) / (err.max() - err.min())
    
    return err


def inout_ratio(err: str, gt: str) -> Union[np.float64, None]:
    in_mask, out_mask = get_gtmask(gt, resize=True)
    err = get_error(err, normalize=True)
    
    if not (in_mask is None):
        in_pixels = np.sum(in_mask)
        out_pixels = np.sum(out_mask)
        
        sum_in_error = np.sum(in_mask*err)
        sum_out_error = np.sum(out_mask*err)
        
        # * integrity check
        # cv2.imwrite('/home/user/Downloads/in.jpg', in_mask*err*255)
        # cv2.imwrite('/home/user/Downloads/out.jpg', out_mask*err*255)
        
        e_out = (1/out_pixels) * sum_out_error
        e_in = (1/in_pixels) * sum_in_error
        
        return e_out / e_in
    else:
        print('GT mask not available')
        
        return None


err = '/home/user/Downloads/error_04_116.png'
gt = '/home/user/Downloads/136.bmp'

res = inout_ratio(err, gt)
print(res)