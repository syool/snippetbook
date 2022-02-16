import torch
import torch.utils.data as data
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.utils as vutils

import numpy as np
from collections import OrderedDict
from glob import glob
from PIL import Image
import os


class WindowLoader(data.Dataset):
    ''' Load a dataset using the silding window '''
    def __init__(self, path, transform, window) -> None:
        super(WindowLoader, self).__init__()
        
        self.path = path
        self.transform = transform
        self.window = window
        self.window_list = self.get_windows()
    
    # get windows from the entire set
    def get_windows(self):
        videos = sorted(glob(os.path.join(self.path, '*')))
        
        entry1 = []
        for vid in videos:
            frames = sorted(glob(os.path.join(vid, '*')))
            entry1.append(frames)
        
        entry2 = []
        for vid in entry1:
            for i in range(len(vid)):
                fr_path = vid[i:i+self.window]
                
                # Cutting tail of a video w.r.t. the window size
                if len(fr_path) < self.window:
                    continue
                else:
                    entry2.append(fr_path)
                    
        return entry2

    def __getitem__(self, index):
        print(index)
        data = self.window_list[index]
        
        stack = []
        for i in data:
            fr = self.transform(Image.open(i)) # [1, H, W]
            x = torch.squeeze(fr) # [H, W]
            
            stack.append(x)
            
        cat = torch.stack(stack, axis=0) # [window, H, W]
        cat = torch.unsqueeze(cat, dim=0) # [1, window, H, W]
        
        return cat

    def __len__(self):
        return len(self.window_list)


batch = 1
epochs = 10
H, W = 256, 256
num_workers = 4
dataset = 'ped2'
main_dir = '/home/user/Documents'
train_folder = f'{main_dir}/VADSET/{dataset}/testing/frames'

train_set = WindowLoader(train_folder,
                        transforms.Compose([
                            transforms.Grayscale(),
                            transforms.Resize((H, W)),
                            transforms.ToTensor(),
                            transforms.Normalize((0.5), (0.5))
                        ]),
                        window=16)

trainloader = data.DataLoader(train_set, batch_size=batch, shuffle=False,
                    num_workers=num_workers, drop_last=False, pin_memory=True)


for epoch in range(epochs):
    print()
    for i, data in enumerate(trainloader):
        input = Variable(data)