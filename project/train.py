# data loading & training

import torch
import torchvision
import torchvision.transforms as transforms

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.utils.tensorboard import SummaryWriter

import model
import utils

import os
# os.chdir('/home/user/Downloads')


# transforms
transform = transforms.Compose(
    [transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))])

# dataset
trainset = torchvision.datasets.FashionMNIST('/home/user/Downloads/mnist',
    download=True,
    train=True,
    transform=transform)
testset = torchvision.datasets.FashionMNIST('/home/user/Downloads/mnist',
    download=True,
    train=False,
    transform=transform)

# dataloaders
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                        shuffle=True, num_workers=2)

testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                        shuffle=False, num_workers=2)

# classes
classes = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot')

# cuda?
print('cuda?: {}'.format(torch.cuda.is_available()))


net = model.Net()
net = net.cuda()
paranet = nn.DataParallel(net) # caution: use a different variable name. see "WARNING"

# WARNING #
# if you want to use nn.DataParallel,
# don't let SummaryWriter functions cotain any DataParalleled model.

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

dataiter = iter(trainloader)
images, labels = dataiter.next()
images,labels = images.cuda(), labels.cuda()

writer = SummaryWriter('./project/runs')
writer.add_graph(net, images) 


running_loss = 0.0
for epoch in range(100):  # 데이터셋을 여러번 반복

    for i, data in enumerate(trainloader, 0):

        # [inputs, labels]의 목록인 data로부터 입력을 받은 후;
        inputs, labels = data
        inputs, labels = inputs.cuda(), labels.cuda()

        # 변화도(Gradient) 매개변수를 0으로 만들고
        optimizer.zero_grad()

        # 순전파 + 역전파 + 최적화를 한 후
        outputs = paranet(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 1000 == 999:    # 매 1000 미니배치마다...
            
            writer.add_histogram('conv1.weight',
                                 net.conv1.weight,
                                 epoch * len(trainloader) + i)
            
            writer.add_histogram('conv2.weight',
                                 net.conv2.weight,
                                 epoch * len(trainloader) + i)
            
            writer.add_histogram('fc1.weight',
                                 net.fc1.weight,
                                 epoch * len(trainloader) + i)
            
            writer.add_histogram('fc2.weight',
                                 net.fc2.weight,
                                 epoch * len(trainloader) + i)
            
            writer.add_histogram('fc3.weight',
                                 net.fc3.weight,
                                 epoch * len(trainloader) + i)

            # ...학습 중 손실(running loss)을 기록하고
            writer.add_scalar('training loss',
                            running_loss / 1000,
                            epoch * len(trainloader) + i)

            # ...무작위 미니배치(mini-batch)에 대한 모델의 예측 결과를 보여주도록
            # Matplotlib Figure를 기록합니다
            writer.add_figure('predictions vs. actuals',
                            utils.plot_classes_preds(net, inputs, labels, classes),
                            global_step=epoch * len(trainloader) + i)
            
            running_loss = 0.0
            
            
print('Finished Training')