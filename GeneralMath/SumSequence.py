from math import log10
import pandas as pd

round_to = 5

def sigma_sequence_summation(function, start, end, print_dataframe):
    """
    Computes the summation of a sequence using sigma notation.
    :param function: a function that takes an number and returns another number
    :param start: the starting index of the summation
    :param end: the ending index of the summation
    :param print: a boolean indicating whether to print the explanation of the results in a DataFrame
    :return: a pandas DataFrame containing the result of each iteration
    """
    result = 0
    data = {'i': [], '->':[], 'a(i)': []}
    for i in range(start, end+1):
        term = function(i)
        result += term
        data['i'].append(i)
        data['->'].append('')
        data['a(i)'].append(round(term, round_to))
    if print_dataframe:
        print(pd.DataFrame(data).to_string(index=False))
    return result

d2 = 0

def fct_fx(x):
    result = log10(1+(1/(10*x + d2)))
    return result


start = 1
end = 9
result = sigma_sequence_summation(fct_fx, start, end, True)
result = round(result, round_to)
print("function: f(x) = log10(1+(1/(10x + " + str(d2) + ")))")
print("sum from i =", start, "to", end, "of f(i)")
print("result  :", result)
