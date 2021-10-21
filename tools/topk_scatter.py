import torch

torch.manual_seed(0)

l = []
for i in range(5):
    a = torch.randperm(10)[:10]
    l.append(a)

l = torch.stack(l)

val, idx = torch.topk(l, k=3, dim=1)
pruned = torch.zeros_like(l).scatter_(1, idx, val)

print()