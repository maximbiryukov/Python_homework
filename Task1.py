# Выводит максимальный отрицательный элемент в массиве

# Вариант 1 быстрее Варианта 2, однако Вариант 1 более требователен к памяти, поскольку происходит множество вызовов метода добавления элементов в список

import random
import cProfile

MIN = -10
MAX = 10
SIZE = 100000
a = [random.randint(MIN, MAX) for _ in range(SIZE)]

# Вариант 1

def max_neg(intlist):
    neg_list = []
    for number in intlist:
        if number < 0:
            neg_list.append(number)
    if not neg_list:
        print('Отрицательных значений тут нет!')
        return 0
    maximum = neg_list[0]
    maxindex = 0
    for number in neg_list:
        if number > maximum:
            maximum = number
        maxindex = intlist.index(maximum)

    print('Максимальный отрицательный элемент: {}, его индекс: {}.'.format(maximum, maxindex))

# SIZE = 100
#100 loops, best of 3: 240 usec per loop
# SIZE = 1000
#100 loops, best of 3: 1.74 msec per loop

cProfile.run('max_neg(a)')

# SIZE = 100000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.028    0.028 <string>:1(<module>)
#         1    0.017    0.017    0.027    0.027 Task1.py:12(max_neg)
#         1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#     47434    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#     47434    0.007    0.000    0.007    0.000 {method 'index' of 'list' objects}

# Вариант 2

def max_neg2(intlist):
    i = 0
    index = -1
    while i < len(intlist):
        if intlist[i] < 0 and index == -1:
            index = i
        elif 0 > intlist[i] > intlist[index]:
            index = i
        i += 1

    if index != -1:
        print('Максимальный отрицательный элемент: {}, его индекс: {}.'.format(intlist[index], index))

# SIZE = 100
# 100 loops, best of 3: 264 usec per loop
# SIZE = 1000
# 100 loops, best of 3: 1.97 msec per loop

cProfile.run('max_neg2(a)')

# SIZE = 100000
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.102    0.102 <string>:1(<module>)
#         1    0.094    0.094    0.102    0.102 Task1.py:38(max_neg2)
#         1    0.000    0.000    0.102    0.102 {built-in method builtins.exec}
#   100001    0.007    0.000    0.007    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
