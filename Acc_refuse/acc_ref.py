from random import uniform
import matplotlib.pyplot as plt
from math import sqrt,pi,exp 
f = lambda x:exp(-(x**2)/2)

N = 1024 * 128
data = []
for _ in range(N):
    x = uniform(-3,3)
    u = uniform(0,1)
    # print(x,f(x))
    # exit()
    if u < f(x):
        data.append(x)
plt.hist(data,bins=128)
plt.savefig('./acc_normal.png')