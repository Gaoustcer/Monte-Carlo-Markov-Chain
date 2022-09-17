import torch
from torch.distributions import Normal
import numpy as np
# mu_list_x = []
from random import random
# mu_list_y = []
# sigma_list_x = []
# sigma_list_y = []
# torch.
mu = []
sigma = []
gamma = 3
K = 6
for _ in range(K):
    mu.append([gamma * random(),gamma * random()])
    sigma.append( [random(),random()])
np.save("mu.npy",np.array(mu))
np.save('sigma.npy',np.array(sigma))


color = ['r','g','b','c','m','y']

N = 1024 
import matplotlib.pyplot as plt
for i in range(K):
    col = color[i]
    x_list = []
    y_list = []
    for _ in range(N):
        point = torch.normal(mu[i],sigma[i])
        x_list.append(point[0])
        y_list.append(point[1])
    plt.scatter(x_list,y_list,s=0.1,c=col)
np.save("data.npy",np.array([x_list,y_list]))
plt.savefig('GMM_groundtruth.png')
