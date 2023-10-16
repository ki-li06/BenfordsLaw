from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd

def plot_dataframe(df: dict):
    print(list(df.keys()))

    indexes = df['index']

    df = df.clear('index')

    """ fig, ax = plt.subplots()
    ax.bar(df['index'], df['actual'], label='Actual')
    ax.bar(df['index'], df['expected'], label='Expected', color='red')
    ax.set_xlabel('Leading Digits')
    ax.set_xticks(df['index'])
    ax.set_ylabel('Frequency')
    ax.set_title('Benford\'s Law')
    ax.legend()
    plt.show() """

    keys = list(df.keys())
    N = len(keys)
    #ind = np.arange(N)  
    ind = N
    width = 0.25
  
    colors = mcolors.TABLEAU_COLORS

    bars = [plt.bar(ind + width*i, df[keys[i]], width, color = colors[i]) for i in range(0, N)]

    """ xvals = [8, 9, 2] 
    bar1 = plt.bar(ind, xvals, width, color = 'r') 
  
    yvals = [10, 20, 30] 
    bar2 = plt.bar(ind+width, yvals, width, color='g') 
  
    zvals = [11, 12, 13] 
    bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')  """
  
    plt.xlabel("distributions") 
    plt.ylabel('percentage') 
    #plt.title("Players Score") 
  
    plt.xticks(ind+width,keys)
    #plt.xticks(ind+width,['2021Feb01', '2021Feb02', '2021Feb03']) 
    plt.legend( (bars), (keys) ) 
    plt.show() 

print("Display.py loaded")
