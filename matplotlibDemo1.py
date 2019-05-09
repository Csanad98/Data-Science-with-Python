# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:11:29 2019

@author: bakos
"""

#import figure canvas
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#import figure artist
from matplotlib.figure import Figure

fig = Figure()

canvas = FigureCanvas(fig)

#create 10000 random numbers using numpy
import numpy as np
x = np.random.randn(10000)

#create an axes artist
ax = fig.add_subplot(111)

#generate histogram of the 10000 numbers
ax.hist(x, 100)

#add a title to the figure and save it
ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
fig.savefig('matplotlibDemo1_histogram.png')