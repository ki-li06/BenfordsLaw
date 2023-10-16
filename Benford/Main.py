from BenfordSequences import fibonacci, collatz, get_primes
import AnalysisBenfordsLaw as bl
from Display import plot_dataframe  
import pandas as pd

results = []
for i in range(1, 10):
    p = (bl.prob_n(10+i)/(bl.prob_n(1)))
    results.append(p)

df = pd.DataFrame({'Digit': range(1, 10), 'Probability': results})
#plot_dataframe(df, 'Digit', 'Probability', 'Benford\'s Law')


fib = fibonacci(1000)
df = bl.benfords_law_dataset(fib)
print(str(df))
plot_dataframe(df)
