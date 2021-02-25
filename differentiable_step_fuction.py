''' differentiable step function '''

# original idea from

# Serra et al, "Overcoming Catastrophic Forgetting
# with Hard Attention to the Task," ICML 2018.

# for the detail, see section 2.4 in the paper

#%%
import numpy as np
import matplotlib.pyplot as plt

smax = 400
B = 9000
sbatch = 64

slist = []
blist = []
for b in range(0,B,sbatch):
    s = 1/smax + (smax-1/smax) * b/B
    slist.append(s)
    blist.append(b)
    print("batch index={}, scaling s={}".format(b,s))
    
plt.plot(blist, slist, label='scaling parameter')
plt.xlabel('batch index (x64)')
plt.ylabel('scaling parameter s')
plt.legend()
plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.array(slist)
y = sigmoid(x)

plt.xlabel('scaling parameter s')
plt.plot(x,y)
plt.show()
#%%