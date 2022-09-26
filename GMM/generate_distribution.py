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
# np.save("mu.npy",np.array(mu))
# np.save('sigma.npy',np.array(sigma))


color = ['r','g','b','c','m','y']

N = 1024
M = 6
from torch.distributions import Categorical
from torch.nn.functional import softmax
import torch
possibility = torch.rand(M)
possibility = softmax(possibility)
cate = Categorical(possibility)
import matplotlib.pyplot as plt
# possiblity = 
from random import choice
# choice(range(5),p=[0.1,0.1,0.1,0.2,0.5])
from tqdm import tqdm
data = []
for _ in tqdm(range(K * N)):
    index = cate.sample().item()
    c = color[index]
    point = torch.normal(torch.tensor(mu[index]),torch.tensor(sigma[index]))
    data.append(point.numpy())
    plt.scatter(point[0],point[1],c=c,s = 0.1)
possibility = possibility.numpy()
np.savez('data.npz',mu=np.array(mu),data = np.array(data),sigma = np.array(sigma),possibility = np.array(possibility))
'''
info:mu,sigma,possibility,origin data
'''
# for i in range(K):
#     col = color[i]
#     x_list = []
#     y_list = []
#     for _ in range(N):
#         point = torch.normal(torch.tensor(mu[i]),torch.tensor(sigma[i]))
#         x_list.append(point[0])
#         y_list.append(point[1])
#     plt.scatter(x_list,y_list,s=0.1,c=col)
# np.save("data.npy",np.array([x_list,y_list]))
plt.savefig('GMM_groundtruth.png')
