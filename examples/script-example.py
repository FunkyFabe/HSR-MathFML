from matplotlib import pyplot
import numpy as np
from numpy import cos, sin

t = np.linspace(-5, 5)  # t is a list of 100 numbers from -10 to 10
p = np.array([[2], [3]])  # p is a 2 dimensional column vector
v = np.array([[1], [-1]]) # v is a 2 dimensional column vector
line = p + t * v          # calculates all points on the line
pyplot.plot(*line, 'b')   # and plots the line in blue
r = 3
circle = p + r * np.array([cos(t), sin(t)]) # calculates points on circle
pyplot.plot(*circle, 'b')                   # and plots the circle in blue

pyplot.plot(*p, 'rx')     # plot the coordinates of p in red
pyplot.axis('equal')      # make both axis of equal scale
pyplot.show()             # show the graph