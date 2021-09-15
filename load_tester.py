import torch
import torch.utils.data as data
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.utils as vutils

import numpy as np
from collections import OrderedDict
import glob
from PIL import Image
import os


def slide(x, window_size):
    entry = []
    for i in range(len(x)-(window_size-1)):
        window = []
        for j in range(i, window_size+i):
            window.append(x[j])
        entry.append(window)

    return entry


class WindowLoader(data.Dataset):
    def __init__(self, data_path, transform, window):
        super(WindowLoader, self).__init__()

        self.dir = data_path
        self.transform = transform
        self.window = window
        self.dict = OrderedDict()
        self.setup()
        self.samples = self.get_samples()
        
    # === create a dictionary ===
    def setup(self):
        videos = glob.glob(os.path.join(self.dir, '*')) # get a path of each video
        for video in sorted(videos):
            video_name = video.split('/')[-1] # get video names
            self.dict[video_name] = {}
            self.dict[video_name]['path'] = video
            self.dict[video_name]['frame'] = glob.glob(os.path.join(video, '*.jpg'))
            self.dict[video_name]['frame'].sort()
            self.dict[video_name]['length'] = len(self.dict[video_name]['frame'])

    # === indexing frames for sliding window ===
    def get_samples(self):
        container = []
        videos = glob.glob(os.path.join(self.dir, '*'))
        for video in sorted(videos):
            video_name = video.split('/')[-1]
            entry = self.dict[video_name]['frame']
            entry = slide(entry, self.window) # -> triple loop: improvement required
            container.extend(entry)
        
        return container

    def __getitem__(self, index):
        data = self.samples[index]
        
        stack = []
        for i in data:
            img = self.transform(Image.open(i))
            img = torch.squeeze(img)
            stack.append(img)
            
        cat = torch.stack(stack, axis=0)
        cat = torch.unsqueeze(cat, dim=0)
        
        return cat

    def __len__(self):
        return len(self.samples)


class FrameLoader(data.Dataset): # PROBLOMETIC SHIIIIT
    def __init__(self, data_path, transform):
        super(FrameLoader, self).__init__()
        
        self.dir = data_path
        self.transform = transform
        self.dict = OrderedDict()
        self.setup()
        self.samples = self.get_samples()

    # === create a dictionary ===
    def setup(self):
        videos = glob.glob(os.path.join(self.dir, '*')) # get a path of each video
        for video in sorted(videos):
            video_name = video.split('/')[-1] # get video names
            self.dict[video_name] = {}
            self.dict[video_name]['path'] = video
            self.dict[video_name]['frame'] = glob.glob(os.path.join(video, '*.jpg'))
            self.dict[video_name]['frame'].sort()
            self.dict[video_name]['length'] = len(self.dict[video_name]['frame'])

    # === list all frames from the entire set ===
    def get_samples(self):
        frames = []
        videos = glob.glob(os.path.join(self.dir, '*'))
        for video in sorted(videos):
            video_name = video.split('/')[-1]
            for i in range(len(self.dict[video_name]['frame'])):
                frames.append(self.dict[video_name]['frame'][i])
                           
        return frames
    
    def __getitem__(self, index):
        video_name = self.samples[index].split('/')[-2]
        frame_name = int(self.samples[index].split('/')[-1].split('.')[-2])
        # print('getitem index:', index)
        
        print(self.dict[video_name]['frame'][frame_name])
        
        image = Image.open(self.dict[video_name]['frame'][frame_name])
        image = self.transform(image)

        return image
    
    def __len__(self):
        return len(self.samples)


batch = 10
epochs = 1
H, W = 256, 256
num_workers = 4
dataset = 'shanghai'
main_dir = '/home/user/Downloads'
train_folder = '{}/VADSET/{}/training/frames'.format(main_dir, dataset)

train_set = FrameLoader(train_folder,
                        transforms.Compose([
                            transforms.Grayscale(),
                            transforms.Resize((H, W)),
                            transforms.ToTensor(), # ! ToTensor before Normalize
                            # transforms.Normalize(mean=[0.5], std=[0.5]),
                        ]))

trainloader = data.DataLoader(train_set, batch_size=batch, shuffle=False,
                    num_workers=num_workers, drop_last=True, pin_memory=True)


for epoch in range(epochs):
    for i, data in enumerate(trainloader):
        input = Variable(data)