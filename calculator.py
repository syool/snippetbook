#%%
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
    print("when b={}:".format(b), s)
    
plt.plot(slist, blist)
plt.show()
#%%