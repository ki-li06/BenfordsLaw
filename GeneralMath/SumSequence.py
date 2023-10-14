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

def get_as_digits(list_digits):
    """
    Converts a list of digits to a number.
    :param list_digits: a list of digits
    :return: the number represented by the list of digits
    """
    result = 0
    for i in range(len(list_digits)):
        result += list_digits[i] * 10 ** (len(list_digits) - i - 1)
    return result

print("SumSequence.py loaded")