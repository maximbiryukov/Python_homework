# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

MIN = 2
MAX = 99
SIZE = 10
a = [random.randint(MIN, MAX) for _ in range(SIZE)]

def even_indexer(intlist): # возвращает список с индексами четных чисел списка - аргумента
    print(intlist)
    evenlist = []
    for number in intlist:
        if number % 2 == 0:
            evenlist.append(intlist.index(number))
    return evenlist

print(even_indexer(a))
