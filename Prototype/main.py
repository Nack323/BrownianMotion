from particle import *
import numpy as np
import matplotlib.pyplot as plt

""" Description of experiment
there will be n particles of the same size and all will have
a momentum and radius. The colission between them will be completely
elastic and they will bounce against walls
 """

n = 250
steps = 2000
DT = 1/60
massMultiplier = 1 # this will be multiplied to the radious cubed so equal density
                   # between all particles is assumed

X = np.arange(1, 9, 0.5)
Y = np.arange(1, 9, 0.5)
CoordList = [(i, j) for i in X for j in Y]
print(f'The maximum number of points is {len(CoordList)}')
if n > len(CoordList):
    exit()

# create particles
particleArray = [Particle(0.08, CoordList[i][0], CoordList[i][1], 
    np.random.rand() * 10 - 5, np.random.rand() * 10 - 5, DT) for i in range(n)]

def particleDistance(a, b):
    xd = a.x - b.x
    yd = a.y - b.y
    return np.linalg.norm([xd, yd])

# create update loop
for i in range(steps):
    # step all particles
    for p in particleArray:
        p.step()
    if i % 10 == 0:
        print(f"{i} done                ", end='\r')
    # check for colission
    for a in range(n):
        for b in range(n):
            if not a == b:
                minDist = particleArray[a].r + particleArray[b].r
                dist = particleDistance(particleArray[a], particleArray[b])
                if dist <= minDist:
                    #calculate new velocities
                    particleArray[a].unstep()
                    particleArray[b].unstep()
                    va = particleArray[a].getVVector()
                    vb = particleArray[b].getVVector()
                    ma = particleArray[a].r ** 3 * massMultiplier
                    mb = particleArray[b].r ** 3 * massMultiplier
                    ra = particleArray[a].pvector
                    rb = particleArray[b].pvector
                    M = ma + mb
                    ua = va - 2 * mb / M * (np.dot((va - vb), (ra - rb)))/(np.linalg.norm(ra - rb) ** 2) * (ra - rb)
                    ub = vb - 2 * ma / M * (np.dot((vb - va), (rb - ra)))/(np.linalg.norm(rb - ra) ** 2) * (rb - ra)
                    particleArray[a].setVVector(ua)
                    particleArray[b].setVVector(ub)
                    #print('aa')
    for particle in particleArray:
        if particle.x > 9.9:
            vx = particle.vx
            vy = particle.vy
            particle.x = 9.9
            particle.setVVector([-vx, vy])
        if particle.x <0.1:
            vx = particle.vx
            vy = particle.vy
            particle.x = 0.1
            particle.setVVector([-vx, vy])
        if particle.y > 9.9:
            vx = particle.vx
            vy = particle.vy
            particle.y = 9.9
            particle.setVVector([vx, -vy])
        if particle.y < 0.1:
            vx = particle.vx
            vy = particle.vy
            particle.y = 0.1
            particle.setVVector([vx, -vy])
    # render and save frame
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    circles = [
        plt.Circle(
            particleArray[i].getPVector(),
            particleArray[i].r
        )
        for i in range(n)
    ]
    
    for c in circles:
        ax.add_patch(c)
    fig.savefig(f"frames/frame{str(i).zfill(4)}.png")
    plt.close(fig)
    del fig, ax

import os
os.system("cd frames; ffmpeg -framerate 60 -pattern_type glob -i '*.png' -c:v libx264 -pix_fmt yuv420p out.mp4")
