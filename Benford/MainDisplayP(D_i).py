from BenfordSequences import fibonacci, collatz, get_primes
import AnalysisBenfordsLaw as bl
from Display import plot_dataframe  
import pandas as pd

results = []
limit = 1 + 3

for i in range(1, limit):
    prob = [bl.prob_d_i(j, i) for j in range(1, 10)]
    results.append(prob)

print(len(results), " columns of data")

df = pd.DataFrame({'index': range(1, 10)})
#plot_dataframe(df, 'Digit', 'Probability', 'Benford\'s Law')


for i in range(0, limit-1):
    values = results[i]
    df.insert(len(df.columns), column=("i="+str(i+1)), value=values)

print(str(df))
plot_dataframe(data_dict=df, title="P(D_i = d)", y_label="Probability", x_label="digit d")


