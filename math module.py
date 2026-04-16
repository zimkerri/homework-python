x = 400
print(math.sqrt(x))

print(pow(5, 3))

from math import pi

print(pi)

print(math.log2(8))
# print(math.log10(100))
import math
#
# import random as r
# son = r.randint(0,100)
# print(son)
#
# ismlar = ['olim', 'anvar', 'hasan', 'husan']
# ism = r.choice(ismlar)
# print(ism)
#
# #
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)
#
# #
#
# sonlar = list(range(11))
# k


import random as r
sonlar = r.sample(range(100), 10)
def juftmi(x):
    return x%2==0
juft_sonlar = list(filter(juftmi, sonlar))
print(sonlar)
print(juft_sonlar)

juft_sonlar2 = list(filter(lambda son:son%2==0, sonlar))
print(sonlar)
print(juft_sonlar2)

mevalar =['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", "qovun", "banan"]
mevalar_b = list(filter(lambda meva:meva.startswith('a'), mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)


