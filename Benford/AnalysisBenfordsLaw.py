from math import log10

import sys

sys.path.append('GeneralMath')
from SumSequence import get_as_digits


def get_first_significant_digit(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Loop through the string until we find a non-zero digit
    for digit in num_str:
        if digit != '0':
            return int(digit)
    
    # If we haven't found a non-zero digit, return 0
    return 0

def benfords_law_dataset(nums: list):
    # Define the expected frequencies of the first significant digits according to Benford's Law
    expected_freqs = {1: 0.301, 2: 0.176, 3: 0.125, 4: 0.097, 5: 0.079, 6: 0.067, 7: 0.058, 8: 0.051, 9: 0.046}

    

    # Initialize a dictionary to count the actual frequencies of the first significant digits
    actual_freqs = {digit: 0 for digit in range(1, 10)}
    
    # Loop through the input list and count the actual frequency of each first significant digit
    for num in nums:
        first_digit = get_first_significant_digit(num)
        actual_freqs[first_digit] += 1
    
    # Normalize the actual frequencies to get the actual frequency percentages
    total_count = len(nums)
    actual_freq_percs = {digit: round(actual_freqs[digit] / total_count, 3) for digit in actual_freqs}
    
    # Return a dictionary with the expected and actual frequency percentages of the first significant digits
    return {'expected': expected_freqs, 'actual': actual_freq_percs}

   
def prob_n(n):
    #Returns the probabilty that a number will start with n/the digits in n
    number = n
    if(type(n) != int):
        number = get_as_digits(n)
    if(number == 0):
        return 0
    return log10(1+(1/(number)))

def prob_d_i(d: int, index: int):
    #return the probabilty that number d is the index's digit
    index = index-1
    #print("index(zerod):", index)
    if(index == 0):
        return prob_n(d)
    listnumbers = [i*10 + d for i in range(10**(index-1), 10**index)]
    #print("listnumbers:", listnumbers)

    sum = 0
    for i in listnumbers:
        n = d + i*10
        sum += prob_n(i)
    return sum

print("AnalysisBenfordsLaw.py loaded")
