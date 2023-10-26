import matplotlib.pyplot as plt
import pandas as pd


def fibonacci(n):
    sequence = [1, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

""" start = int(
    "815355251516374308149911284638621926267603755059081996059706919298081532083617454274742447036265896665369512070149"
    + "5705518391947130985569167260370122584434931877771920539034280455223811019363391529801501383882238293855716834055778"
    + "6864220648065504475745782625457481458374625761278786642868836574239844192810797681135941491892710383464715906173845"
    + "5223958742086902601591850005819607758559839170847116339379629176980725238387269848449469772233714493713817585453615"
    + "5301276961056843068280190398074124823945345973686574174080802905749395516482371128893884283040802881082819776404394"
    + "7396425144820569462155814176665643619626065404545327988122649046580684251190783991014372801125254211290128159679741"
    + "029773296815391789593534745183667443659575044334622833950600623946057166892463091687535351429312347992622951499")
# length 22503 """

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def getCollatzLength(n):
    length = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

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
