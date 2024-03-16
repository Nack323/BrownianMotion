from particle import *
import numpy as np

""" Description of experiment
there will be n particles of the same size and all will have
a momentum and radius. The colission between them will be completely
elastic and they will bounce against walls
 """

n = 10

particleArray = [Particle(0.1, np.random(), np.random(), 
    np.random(), np.random(), 0.01)]
