from math import log10

import sys

sys.path.append('GeneralMath')
from SumSequence import get_as_digits


def get_first_significant_digits(num, amount = 1):
    # Convert the number to a string
    num_str = str(num)
    num_str = num_str.replace('.', '') + "0" * amount

    
    # Loop through the string until we find a non-zero digit
    for i in range(len(num_str)):
        if num_str[i] != '0':
            return int(num_str[i: i + amount])    
    # If we haven't found a non-zero digit, return 0
    return 0


def benfords_law_on_dataset(nums: list, digits: int = 1):
    # Define the expected frequencies of the first significant digits according to Benford's Law
    myrange = range(10**(digits-1), 10**digits)

    expected_freqs = {digit: prob_n(digit) for digit in myrange}
    

    # Initialize a dictionary to count the actual frequencies of the first significant digits
    actual_freqs = {digit: 0 for digit in myrange}
    
    # Loop through the input list and count the actual frequency of each first significant digit
    for num in nums:
        first_digit = get_first_significant_digits(num, digits)
        actual_freqs[first_digit] += 1
    
    # Normalize the actual frequencies to get the actual frequency percentages
    total_count = len(nums)
    actual_freq_percs = {digit: round(actual_freqs[digit] / total_count, 3) for digit in actual_freqs}
    
    # Return a dictionary with the expected and actual frequency percentages of the first significant digits
    return {'index': myrange,'expected': expected_freqs, 'actual': actual_freq_percs}

   
def prob_n(n):
    #Returns the probabilty that a number will start with n / the digits in n
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
