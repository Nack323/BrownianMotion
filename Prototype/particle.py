
class Particle:

    def __init__(self, r, x, y, vx, vy, dt):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.dt = dt
        self.r = r

    def step(self):
        self.x = self.x + self.dt * self.vx 
        self.y = self.y + self.dt * self.vy 

    def unstep(self): # probably unnecessary
        self.x = self.x - self.dt * self.vx 

    def getPos(self):
        return self.x, self.y
