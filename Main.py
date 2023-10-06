from Sequences import fibonacci, collatz
from AnalysisBenfordsLaw import benfords_law as bl
import pandas as pd

n_fib = 50

fib = fibonacci(n_fib)
print("First " + str(n_fib) + " Fibonacci numbers: " + (str(fib)[1:-1] if len(fib) < 10 else str(fib[:10])[1:-1] + ", ..."))

bl_fib = bl(fib)
df = pd.DataFrame({'expected': bl_fib['expected'], 'actual': bl_fib['actual']})
print(df)

n_collatz = 1324354657687980

coll = collatz(n_collatz)
print("Collatz sequence from " + str(n_collatz) + " (len: " + str(len(coll)) + "): " + (str(coll)[1:-1] if len(coll) < 10 else str(coll[:10])[1:-1] + ", ..."))

bl_coll = bl(coll)
df = pd.DataFrame({'expected': bl_coll['expected'], 'actual': bl_coll['actual']})
print(df)
