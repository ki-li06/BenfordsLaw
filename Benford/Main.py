from math import modf
from random import randint

from AnalysisBenfordsLaw import benfords_law_on_dataset
from Display import plot_dataframe, print_as_dataframe
from BenfordSequences import collatz, getCollatzLength

i_max = 1
c_i_max = 1

print("start loop of collatz sequences")

start = int(
    "815355251516374308149911284638621926267603755059081996059706919298081532083617454274742447036265896665369512070149"
    + "5705518391947130985569167260370122584434931877771920539034280455223811019363391529801501383882238293855716834055778"
    + "6864220648065504475745782625457481458374625761278786642868836574239844192810797681135941491892710383464715906173845"
    + "5223958742086902601591850005819607758559839170847116339379629176980725238387269848449469772233714493713817585453615"
    + "5301276961056843068280190398074124823945345973686574174080802905749395516482371128893884283040802881082819776404394"
    + "7396425144820569462155814176665643619626065404545327988122649046580684251190783991014372801125254211290128159679741"
    + "029773296815391789593534745183667443659575044334622833950600623946057166892463091687535351429312347992622951499")
# length 22503
print("start: " + str(start))
mylist = collatz(start)
limit = int(start/(10**1000))
for i in range(1, limit):
    collatz_list = collatz(start + i)
    for c in collatz_list:
        mylist.append(c)
print("the collatz sequence of " + str(start) + " is " + str(mylist[:20]) + ",... (length: " + str(len(mylist)) + ")")

benford = benfords_law_on_dataset(mylist, 2)
print(benford["index"])
plot_dataframe(benford, x_label="First digit", y_label="Frequency", title="Benford's law on the Collatz sequence (" + str(len(mylist)) + " elements)")


i_top = 1
i_length = 1

exponent = 800

while True:
    #print("loop")
    start = randint(10**(exponent), 10**(exponent + 1))
    #print("start: " + str(start))
    length = getCollatzLength(start)
    if(i_length < length):
        i_top = start
        i_length = length
        print("New record: i= " + str(i_top) + " --> " + str(i_length))