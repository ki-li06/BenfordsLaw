import matplotlib.pyplot as plt
import pandas as pd


def fibonacci(n):
    sequence = [1, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

"""
n_fib = 50

fib = fibonacci(n_fib)
print("First " + str(n_fib) + " Fibonacci numbers: " + (str(fib)[1:-1] if len(fib) < 10 else str(fib[:10])[1:-1] + ", ..."))

bl_fib = bl(fib)
df = pd.DataFrame({'expected': bl_fib['expected'], 'actual': bl_fib['actual']})
print(df)
plot_dataframe(df)
"""

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

""" n_collatz = 1324354657687980

coll = collatz(n_collatz)
print("Collatz sequence from " + str(n_collatz) + " (len: " + str(len(coll)) + "): " + (str(coll)[1:-1] if len(coll) < 10 else str(coll[:10])[1:-1] + ", ..."))

bl_coll = bl(coll)
df = pd.DataFrame({'expected': bl_coll['expected'], 'actual': bl_coll['actual']})
print(df) """

def get_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        #print("in loop")
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            if n > 10**4 and len(primes) % (n/10) == 0:
                print("found " + str(len(primes)) + " primes")
        num += 1
    return primes


print("BenfordSequences.py loaded")
