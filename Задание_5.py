# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

import random

MIN = -10
MAX = 10
SIZE = 10
a = [random.randint(MIN, MAX) for _ in range(SIZE)]

def max_neg(intlist):
    print(intlist)
    neg_list = []
    for number in intlist:
        if number < 0:
            neg_list.append(number)
    if not neg_list:
        print('Отрицательных значений тут нет!')
        return 0
    print(neg_list)
    maximum = neg_list[0]
    maxindex = 0
    for number in neg_list:
        if number > maximum:
            maximum = number
        maxindex = intlist.index(maximum)

    print('Максимальный отрицательный элемент: {}, его индекс: {}.'.format(maximum, maxindex))

max_neg(a)