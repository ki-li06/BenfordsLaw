from math import log10
from SumSequence import sigma_sequence_summation, get_as_digits

round_to = 5

d2 = 0

def fct_fx(x):
    result = log10(1+(1/(10*x + d2)))
    return result


start = 2
end = 9
result = sigma_sequence_summation(fct_fx, start, end, True)
result = round(result, round_to)
print("function: f(x) = log10(1+(1/(10x + " + str(d2) + ")))")
print("sum from i =", start, "to", end, "of f(i)")
print("result  :", result)

print("-"*50)

digits = [2, 5, 7]
n = get_as_digits(digits)
print("digits  :", digits, "=>", n)
