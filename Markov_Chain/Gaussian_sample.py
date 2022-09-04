from torch.distributions import Normal
possibility = {}
count = {}
def key(x):
    if x > 0:
        for i in range(6):
            if x > (5-i):
                return 5-i
    for i in range(6):
        if x < i - 5:
            return i - 5
    print("Error x is ",x)
    raise ValueError

normal = Normal(0,1)
Samplenum = 1024 * 1024

for i in range(-5,6):
    count[i] = 0
import numpy as np
from tqdm import tqdm
for _ in tqdm(range(Samplenum)):
    sample = normal.sample()
    key_ = key(sample)
    count[key_] += 1
for key in count.keys():
    possibility[key] = count[key]/sum(count.values())
import json
with open('poss.json','w') as fp:
    json.dump(possibility,fp,indent=1)