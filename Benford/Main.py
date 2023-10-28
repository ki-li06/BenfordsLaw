from math import log10, modf
from random import randint

import pandas as pd

from AnalysisBenfordsLaw import benfords_law_on_dataset
from Display import plot_dataframe, print_as_dataframe
from BenfordSequences import collatz, getCollatzLength


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    digits = digits[::-1]
    text = ""
    for i in digits:
        text += str(i)
    return int(text)

n_max = 100
base = 1
myrange = pd.Series(list(range(1, n_max+1)))
mylist = list([2**i for i in myrange])
print("mylist:", mylist)
mylist = [numberToBase(i, 3) for i in mylist]
print("mylist:", mylist)

benford = benfords_law_on_dataset(mylist)
print_as_dataframe(benford)

#print(int(str(n), base=2))