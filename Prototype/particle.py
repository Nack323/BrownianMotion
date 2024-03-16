
class Particle:

    def __init__(self, x, y, vx, vy, dt):
        self.x = x;
        self.y = y;
        self.vx = vx;
        self.vy = vy;

    def step():
        self.x = self.x + self.dt * self.vx 
        self.y = self.y + self.dt * self.vy 

    def getPos():
        return self.x, self.y
