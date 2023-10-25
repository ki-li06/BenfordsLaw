from math import modf
from random import randint

from AnalysisBenfordsLaw import benfords_law_on_dataset
from Display import plot_dataframe, print_as_dataframe
from BenfordSequences import collatz, getCollatzLength

i_max = 1
c_i_max = 1

print("start loop of collatz sequences")

def collatz_short(n):
    sequence = [n]
    while n != 1:
        n = 3*n + 1
        while(n%1 == 0):
            n /= 2
        n = int(n*2)
        sequence.append(n)
    return sequence

start = int(
    "240778212380227069166211756689069994820018718445226482376563776225594502920847664101182"
    + "7057579794814128183666218543096098219306400681450327221774080184072819216543265612213921"
    + "0344562907106627109103393827467060011947393878162341725448794609029390212862341230134287"
    + "93627310283049010204079181085430823355536670829766818670229290897248990319215764096677269"
    + "3620139834174559319177848991496846960629964285318")
# length 11285
print("start: " + str(start))
mylist = collatz(start)
print("the collatz sequence of " + str(start) + " is " + str(mylist[:20]) + ",... (length: " + str(len(mylist)) + ")")

benford = benfords_law_on_dataset(mylist, 2)
print(benford["index"])
plot_dataframe(benford)


i_top = 1
i_length = 1

exponent = 400

while True:
    #print("loop")
    start = randint(10**(exponent), 10**(exponent + 1))
    #print("start: " + str(start))
    length = getCollatzLength(start)
    if(i_length < length):
        i_top = start
        i_length = length
        print("New record: i= " + str(i_top) + " --> " + str(i_length))