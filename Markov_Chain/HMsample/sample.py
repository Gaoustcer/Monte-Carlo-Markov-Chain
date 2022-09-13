from torch.distributions import Normal
normalsampler = Normal(0,1)
import matplotlib.pyplot as plt
N = 1024 * 8
def _baseline():
    data = normalsampler.sample((N,))
    plt.hist(data,bins=128)
    plt.savefig('baseline.png')
    plt.close()
from math import sqrt
from math import pi
from math import exp
def _possibility(x):
    return 1/(sqrt(2*pi))*exp(-(x**2/2))


State_transtiontime = 16
from random import random
expparamter = 6
base = 0.5
def _next_state(current_state):
    next_candidatestate = expparamter * (random() - base)
    current_possibility = _possibility(current_state)
    next_possibility = _possibility(next_candidatestate)
    rate = next_possibility/current_possibility
    if random() < rate:
        # print("state change")
        return next_candidatestate
    else:
        return current_state

def HMsample():
    data = []
    from tqdm import tqdm
    for _ in tqdm(range(N)):
        state = expparamter * (random() - base)
        for _ in range(State_transtiontime):
            state = _next_state(state)
        data.append(state)
    plt.hist(data,bins=128)
    # print(data[:64])
    plt.savefig("HM.png")




if __name__ == "__main__":
    # _baseline()
    HMsample()