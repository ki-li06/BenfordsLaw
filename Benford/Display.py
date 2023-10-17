from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd

# BEGIN: yzj1z5v9jz7a
def plot_dataframe(data_dict, title = "", y_label = "", x_label = "d"):
    """
    Plots a bar chart for the data in the dictionary with the indexes as the x-axis title.

    Parameters:
    data_dict (dict): A dictionary with columns index and columns with other data.

    Returns:
    None
    """
    index = data_dict['index']
    keys = list(data_dict.keys())
    keys.remove('index')


    names = keys
    vals = [data_dict[key] for key in keys]
    colors = list(mcolors.TABLEAU_COLORS)
    indexes = index

    N = len(index)
    ind = np.arange(N)
    dist = 2
    ind = ind * dist
    #print("ind: ", ind)
    width = (dist-0.3)/len(vals)

    bars = []

    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.grid(zorder=0)

    for i in range(len(vals)):
        values = vals[i]
        color = colors[i]
        bar = plt.bar(x=(ind + width*i), height=values, width=width, color=color, zorder=3)
        bars.append(bar)

    tick_move = (width*(len(vals)-1))/2
    #print("tick_move: ", tick_move)
    ticks_x = ind + tick_move
    #print("ticks_x: ", ticks_x)
    plt.xticks(ticks_x, indexes) 
    plt.legend( list(bars), list(names) ) 
    plt.show() 
    # END: yzj1z5v9jz7a

print("Display.py loaded")
