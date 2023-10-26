from math import log10, modf
from random import randint

from AnalysisBenfordsLaw import benfords_law_on_dataset
from Display import plot_dataframe, print_as_dataframe
from BenfordSequences import collatz, getCollatzLength


expo = 2.5
mylist = []
for i in range(1, 10**8):
    if(log10(i) % 1 == 0):
        print("i: 10**" + str(int(log10(i))))
    mylist.append(i**expo)

print("mylist: ", (mylist[:10]))
print("length: ", len(mylist))


benford = benfords_law_on_dataset(mylist)
print("benford: ", benford)
print("type: ", type(benford))
print_as_dataframe(benford)
plot_dataframe(benford, title="Benford's Law on the expo" + str(expo), y_label="Probability (%)", x_label="d")