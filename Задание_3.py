# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

MIN = 2
MAX = 99
SIZE = 10
a = [random.randint(MIN, MAX) for _ in range(SIZE)]

def mm_swapper(intlist): # меняет местами мин и макс числа списка - аргумента
    minimum = intlist[0]
    maximum = intlist[0]
    minindex = 0
    maxindex = 0
    for number in intlist:
        if number > maximum:
            maximum = number
            maxindex = intlist.index(number)
        if number < minimum:
            minimum = number
            minindex = intlist.index(number)
    intlist[maxindex] = minimum
    intlist[minindex] = maximum

print(a)
mm_swapper(a)
print(a)
