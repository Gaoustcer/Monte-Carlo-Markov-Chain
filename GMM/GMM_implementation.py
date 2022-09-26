import numpy as np

K = 6

from torch.utils.tensorboard import SummaryWriter
from torch.nn.functional import softmax
from scipy.stats import multivariate_normal as multi_normal
import torch
writerlog = "./log/GMM"
class GMMAgent:
    def __init__(self) -> None:
        self.K = K
        self.possibility = softmax(torch.rand(self.K))
        self.writer = SummaryWriter(writerlog)
        self.mu = torch.rand((self.K,2))
        self.sigma = torch.rand((self.K,2))
        self.data = torch.from_numpy(np.load('data.npz')['data'])
        self.pointspossibility = torch.zeros((self.data.shape[0],self.K))
        
        # self.groundtruthmu = sel
    
    def Estep(self):
        '''
        计算每个数据点属于每个分布的概率
        p_{ij} =\frac{pi_i N(X_i|\mu_j,\sima_j)}{\sum_{k=1}^K pi_k N(X_i|\mu_k,\sigma_k)},
        p_{ij}数据点i属于高斯分布j的概率
        '''
        for i in range(K):
            self.pointspossibility[:,i] = torch.from_numpy(multi_normal.pdf(self.data,self.mu[i],self.sigma[i]))
        self.pointspossibility /= torch.sum(self.pointspossibility,-1).unsqueeze(-1)
        print(self.pointspossibility[0])
    
    def MStep(self):
        '''
        根据概率$p_ij$计算新的聚类中心/计算均值和方差
        均值$mu_j = \sum_i p_ij x_i$
        方差$sigma_j = \sum_i p_ij (x_i-mu_j) $
        '''
        for i in range(self.K):
            # P = self.possibility[:,i]
            P = self.pointspossibility[:,i]
            x = self.data[:,0]
            y = self.data[:,1]
            self.mu[i] = torch.tensor([x.dot(P),y.dot(P)])/P.sum()
            print(self.mu[i])
            self.sigma[i] = torch.einsum('ij,i->j',[(self.data - self.mu[i])**2,P])
    

    def learn(self):
        EPOCH = 128
        from tqdm import tqdm
        for epoch in tqdm(range(EPOCH)):
            self.Estep()
            self.MStep()
            self.writer.add_scalar('mu_x',self.mu[0][0],epoch)
            self.writer.add_scalar('mu_y',self.mu[0][1],epoch)
        self.possibility = self.pointspossibility.mean(0)
        # for i in range(self.K):
        #     self.possibility[i] = self.pointspossibility[:,i]
            
if __name__ == "__main__":
    Agent = GMMAgent()
    Agent.learn()

        

