from Sequences import fibonacci, collatz, get_primes
from AnalysisBenfordsLaw import benfords_law as bl_analysis, prob as bl_prob
from Display import plot_dataframe  
import pandas as pd
import sys

list_d = [3, 1, 4]

p = bl_prob(list_d)

print("list_d: " + str(list_d) + " => " + str(p))
