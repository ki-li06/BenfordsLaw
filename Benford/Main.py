from BenfordSequences import fibonacci, collatz, get_primes
import AnalysisBenfordsLaw as bl
from Display import plot_dataframe  
import pandas as pd

print("load primes")
primes = get_primes(100000)
print("primes loaded")
benford = bl.benfords_law_dataset(primes)

print(benford)

plot_dataframe(benford, "primes")


print("Main.py loaded")