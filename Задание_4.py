# Определить, какое число в массиве встречается чаще всего.

import random

MIN = 2
MAX = 10
SIZE = 100
a = [random.randint(MIN, MAX) for _ in range(SIZE)]

def freq_int(intlist): # возвращает число, чаще всего встречающееся в списке - аргументе
    intset = set(intlist)
    intdict = {}
    for item in intset:
        intdict[item] = 0
    for item in intlist:
        intdict[item] += 1
    print(intdict)
    x = sorted(intdict, key=(lambda key:intdict[key]), reverse=True)
    return x[0]

print(freq_int(a))
