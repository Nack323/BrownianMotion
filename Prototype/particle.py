import numpy as np

class Particle:

    def __init__(self, r, x, y, vx, vy, dt):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.dt = dt
        self.r = r
        self.pvector = np.array([self.x, self.y])
        self.vvector = np.array([self.vx, self.vy])

    def step(self):
        self.x = self.x + self.dt * self.vx 
        self.y = self.y + self.dt * self.vy 
        self.pvector = np.array([self.x, self.y])
        self.vvector = np.array([self.vx, self.vy])

    def unstep(self): # probably unnecessary
        self.x = self.x - self.dt * self.vx 
        self.y = self.y - self.dt * self.vy 
        self.pvector = np.array([self.x, self.y])
        self.vvector = np.array([self.vx, self.vy])

    def getPos(self):
        return self.x, self.y
    
    def getPVector(self):
        return self.pvector
    
    def getVVector(self):
        return self.vvector
    
    def setVVector(self, v):
        self.vx = v[0]
        self.vy = v[1]
        self.pvector = np.array([self.x, self.y])
        self.vvector = np.array([self.vx, self.vy])
