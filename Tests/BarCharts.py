import numpy as np 
import matplotlib.pyplot as plt 

names = ['Player1', 'Player2', 'Player3']
vals = [[8, 9, 2], [10, 20, 30], [11, 12, 13]]
colors = ['r', 'g', 'b']
indexes = ['2021Feb01', '2021Feb02', '2021Feb03']

N = len(names)
ind = np.arange(N) 
width = 0.25
print("ind:", ind)

bars = []

for i in range(len(vals)):
    bars.append(plt.bar(ind + width*i, vals[i], width, color=colors[i]))

plt.xlabel("Dates") 
plt.ylabel('Scores') 
plt.title("Players Score") 

plt.xticks(ind+width,indexes) 
plt.legend( list(bars), list(names) ) 
plt.show() 
