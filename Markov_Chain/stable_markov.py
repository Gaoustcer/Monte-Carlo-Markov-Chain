from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter('../log/')
import numpy as np

transmit_possibility = np.array(
    [[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]]
)
from random import random
from random import randint
def _trans(initstate):
    rand = random()
    if rand < transmit_possibility[initstate][0]:
        return 0
    elif rand < sum(transmit_possibility[initstate][:2]):
        return 1
    else:
        return 2
testtimes = 256 ** 2
count = {0:0,1:0,2:0}
transmittime = 1024
from tqdm import tqdm
for epoch in tqdm(range(testtimes)):
    initstate = randint(0,2)
    for _ in range(transmittime):
        initstate = _trans(initstate)
    count[initstate] += 1
    for i in range(3):
        writer.add_scalar('ratio'+str(i),count[i]/sum(count.values()),epoch)
