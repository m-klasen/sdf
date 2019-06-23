import numpy as np

class Kalman(object):
    def __init__(self, P=None, F=None,D=None,H=None,R=None):
        self.F = F
        self.H = H
        self.P = P
        
        self.D = np.eye(3) if D is None else D
        self.R = np.eye(3) if R is None else R
        self.x = [np.zeros((3, 1)),np.zeros((3, 1))]

        self.P_l = []
        self.x_l = []

    def predict(self):
        self.x = [self.F @ self.x[0], self.F @ self.x[1]]
        self.P = self.F @ self.P @ self.F.T +self.D
        self.P_l.append(self.P)
        self.x_l.append(self.x)
        return [self.x, self.P]

    def update(self, z):
        v = [z[0] - (self.H @ self.x[0]),z[1] - (self.H @ self.x[1])]
        S = self.H @ self.P @ self.H.T  + self.R 
        W = self.P @ self.H.T @ np.linalg.inv(S)
        self.P = self.P- (W @ S @ W.T)
        self.x = [self.x[0]+(W @ v[0]),self.x[1]+(W @ v[1])]

    def retrodict(self, n):
        W = P_l[-(2+n)]  @ self.F.T @ np.linalg.inv(P_l[-(1+n)])
        self.x_l_k = self.x_l[-(2+n)] + W @ (self.x - self.x_l[-(1+n)])
        self.P_l_k = self.P_l[-(2+n)] + W @ (self.P_l_k - self.P_l[-(1+n)]) @ W.T
        return self.x_l

