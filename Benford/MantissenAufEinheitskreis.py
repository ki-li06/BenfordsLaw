from math import log10, modf
from random import randint, random
from matplotlib import pyplot as plt

import pandas as pd
import numpy as np

from AnalysisBenfordsLaw import benfords_law_on_dataset
from Display import plot_dataframe, print_as_dataframe
from BenfordSequences import collatz, fibonacci, getCollatzLength


#mylist = {i for i in range(1, 100)}
mylist = fibonacci(1000)
print(mylist)

mantissas = [modf(log10(i))[0] for i in mylist]
print(mantissas)
mantissas = [i*2*np.pi for i in mantissas]
print(mantissas)

quarter_points_x = [1, 0, -1, 0]
quarter_points_y = [0, 1, 0, -1]
digits_points_x = [np.cos(modf(log10(i))[0]*2*np.pi) for i in range(1, 10)]
digits_points_y = [np.sin(modf(log10(i))[0]*2*np.pi) for i in range(1, 10)]


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x0, y0, dx, dy = ax.get_position().bounds
maxd = max(dx, dy)
width = 6 * maxd / dx
height = 6 * maxd / dy

fig.set_size_inches((width, height))

ax.plot(np.cos(mantissas), np.sin(mantissas), linewidth=0, marker='o', markersize=3, color='green')
ax.plot(quarter_points_x, quarter_points_y, linewidth=0, marker='o', markersize=5, color='blue')
ax.plot(digits_points_x, digits_points_y, linewidth=0, marker='o', markersize=5, color='red')
circ = plt.Circle((0, 0), radius=1, edgecolor='b', facecolor='None')
ax.add_patch(circ)


plt.show()