from math import log10

def get_first_significant_digit(num):
    # Convert the number to a string
    num_str = str(num).replace('.', '')

    
    # Loop through the string until we find a non-zero digit
    for i in range(len(num_str)):
        if num_str[i] != '0':
            return int(num_str[i])    
    # If we haven't found a non-zero digit, return 0
    return 0


def benfords_law_on_list(nums: list):
    # Define the theoretic frequencies of the first significant digits according to Benford's Law
    myrange = {x for x in range(1, 10)}

    theoretic_freqs = {digit: prob_n(digit) for digit in myrange}
    

    # Initialize a dictionary to count the actual frequencies of the first significant digits
    actual_freqs = {digit: 0 for digit in myrange}
    
    # Loop through the input list and count the actual frequency of each first significant digit
    for num in nums:
        first_digit = get_first_significant_digit(num)
        if(first_digit != 0):
            actual_freqs[first_digit] += 1
    
    # Normalize the actual frequencies to get the actual frequency percentages
    total_count = len(nums)
    actual_freq_percs = {digit: round(actual_freqs[digit] / total_count, 5) for digit in actual_freqs}
    
    # Return a dictionary with the theoretic and actual frequency percentages of the first significant digits
    return {'index': myrange,'theoretic': theoretic_freqs, 'actual': actual_freq_percs}

def get_biggest_difference(dict: dict):
    #Returns the highest difference between the exp and theoretic values
    highest_dif = 0
    for i in dict['index']:
        dif = abs(dict['actual'][i] - dict['theoretic'][i])
        if(dif > highest_dif):
            highest_dif = dif
    return highest_dif

def get_as_number(list_digits):
    """
    Converts a list of digits to a number.
    """
    return sum([list_digits[i] * 10 ** (len(list_digits) - i - 1) for i in range(len(list_digits))])

def prob_n(n):
    #Returns the probabilty that a number will start with n / the digits in n
    number = n
    if(type(n) != int):
        number = get_as_number(n)
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

    return sum({prob_n(n) for n in listnumbers})

print("BenfordsLaw.py loaded")
