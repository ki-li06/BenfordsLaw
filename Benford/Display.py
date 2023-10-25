from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd


def print_as_dataframe(data_dict):
    """
    Prints the data in the dictionary as a dataframe.

    Parameters:
    data_dict (dict): A dictionary with columns index and columns with other data.

    Returns:
    None
    """
    df = pd.DataFrame(data_dict)
    print(df)

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
        values = list(vals[i].values())
        #print("values: ", values)
        color = colors[i]
        bar = plt.bar(x=(ind + width*i), height=values, width=width, color=color, zorder=3)
        bars.append(bar)

    tick_move = (width*(len(vals)-1))/2
    #print("tick_move: ", tick_move)
    ticks_x = ind + tick_move
    #print("ticks_x: ", ticks_x)
    used_indexes = []
    used_ticks_x = []
    print("indexes: " + str({i for i in indexes}) + "(" + str(len(indexes)) + ")")
    if len(indexes) < 20:
        used_indexes = indexes
        used_ticks_x = ticks_x
    else:
        length = len(indexes)
        indexes_wanna_use = []
        for i in range(0, length):
            if i%(length/10) == 0:
                indexes_wanna_use.append(i)
                #used_ticks_x.append(ticks[list(indexes)])
        indexes_wanna_use.append(length-1)
        print("indexes_wanna_use: " + str(indexes_wanna_use))
        for i in indexes_wanna_use:
            used_indexes.append(indexes[i])
            used_ticks_x.append(ticks_x[i])

    print("used_indexes: " + str(used_indexes))
        

    plt.xticks(used_ticks_x, used_indexes) 
    plt.legend( (bars), list(names) ) 
    plt.show() 
    # END: yzj1z5v9jz7a

print("Display.py loaded")
