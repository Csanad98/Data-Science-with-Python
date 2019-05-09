# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:27:38 2019

@author: bakos
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)

plt.hist(x, 100)
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
plt.savefig('matplotlibDemo2_histogram.png')
plt.show()