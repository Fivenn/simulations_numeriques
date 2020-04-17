import numpy
import random
from matplotlib import pyplot

N_STEPS = 1000
prob = 0.5

def RandomWalk(N,p,line):
    position = numpy.empty(N)
    position[0] = 0
    pos_counter = 0
    steps = numpy.arange(N)
    for i in range(1,N):
        test = random.random()
        if test >= p:
            pos_counter += 1
        else:
            pos_counter -= 1
        position[i] = pos_counter
    pyplot.plot(steps, position, line)
    return None

pyplot.figure()
pyplot.xlabel('Steps taken')
pyplot.ylabel('Distance from Starting Position')
RandomWalk(N_STEPS, prob, line = 'o--')
pyplot.show()
