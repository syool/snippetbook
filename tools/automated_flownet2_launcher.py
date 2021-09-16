from argparse import RawDescriptionHelpFormatter
import os

# === indexing ===

# index = []
# for i in range(16):
#     a = '{}'.format(i+1)
#     index.append(a.zfill(2))
    
# print(index)

dataset = 'shanghai'
train_test = 'training'
root = '/flownet2-pytorch/VADSET/{}/{}/frames'.format(dataset, train_test)

index = sorted(os.listdir(root))
print(index)

# === launch flownet2 in a loop ===

try:
    for i in range(len(index)):
        
        # == launch flownet2 ==
        
        launcher = 'python3 main.py --inference --model FlowNet2 \
            --save_flow --inference_dataset ImagesFromFolder \
            --inference_dataset_root {}/{} \
            --inference_visualize \
            --resume /flownet2-pytorch/FlowNet2_checkpoint.pth.tar'.format(root, index[i])
        os.system(launcher)
        
        # == chmod created files ==
        
        chmod1 = 'chmod -R 777 /flownet2-pytorch/work/inference/run.epoch-0-flow-field'
        chmod2 = 'chmod -R 777 /flownet2-pytorch/work/inference/run.epoch-0-flow-vis'
        os.system(chmod1)
        os.system(chmod2)
        
        # == change created file names ==
        
        chname1 = 'mv /flownet2-pytorch/work/inference/run.epoch-0-flow-field \
            /flownet2-pytorch/work/inference/flo{}'.format(index[i])
        chname2 = 'mv /flownet2-pytorch/work/inference/run.epoch-0-flow-vis \
            /flownet2-pytorch/work/inference/vis{}'.format(index[i])
        os.system(chname1)
        os.system(chname2)

    print('DONE')
    
except KeyboardInterrupt:
    StopIteration