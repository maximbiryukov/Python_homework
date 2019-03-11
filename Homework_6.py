import random
import sys

# Вывод: Вариант 2 наиболее экономичен в вопросах расходования памяти, а все благодаря минимизации количества переменных и отсутствии необходимости собирать новые списки.

MIN = -10
MAX = 10
SIZE = 10
a = [random.randint(MIN, MAX) for _ in range(SIZE)]

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

# Вариант 1
def max_neg(intlist):
    neg_list = []
    for number in intlist:
        if number < 0:
            neg_list.append(number)
    if not neg_list:
        print('Отрицательных значений тут нет!')
        a = sys.getsizeof(intlist)
        count_intlist = sum([sys.getsizeof(item) for item in intlist])
        b = sys.getsizeof(neg_list)
        count_neglist = sum([sys.getsizeof(item) for item in neg_list])
        c = sys.getsizeof(number)
        print('Эта великолепная функция скушала {} байт памяти (включая лист-аргумент)!'.format(a + b + count_intlist + count_neglist))
        return 0
    maximum = neg_list[0]
    maxindex = 0
    for number in neg_list:
        if number > maximum:
            maximum = number
        maxindex = intlist.index(maximum)
    a = sys.getsizeof(intlist)
    b = sys.getsizeof(neg_list)
    count_intlist = sum([sys.getsizeof(item) for item in intlist])
    count_neglist = sum([sys.getsizeof(item) for item in neg_list])
    c = sys.getsizeof(maximum)
    d = sys.getsizeof(maxindex)
    e = sys.getsizeof(number)
    print('Максимальный отрицательный элемент: {}, его индекс: {}.'.format(maximum, maxindex))
    print('Эта великолепная функция скушала {} байт памяти (включая лист-аргумент)!'.format(a + b + count_intlist + count_neglist + c + d + e))
    return 0

# Вариант 2
def max_neg2(intlist):
    maxneg = -float('inf')
    for item in intlist:
        if item > maxneg and item < 0:
            maxneg = item
    if maxneg == -float('inf'):
        print('Отрицательных значений тут нет!')
    else:
        print('Максимальный отрицательный элемент: {}, его индекс: {}.'.format(maxneg, intlist.index(maxneg)))
    a = sys.getsizeof(intlist)
    count_intlist = sum([sys.getsizeof(item) for item in intlist])
    b = sys.getsizeof(maxneg)
    c = sys.getsizeof(item)
    print('Эта великолепная функция скушала {} байт памяти (включая лист-аргумент)!'.format(a + b + count_intlist + c))
    return 0



# Вариант 3
def max_neg3(intlist):
    neg_list = []
    for item in intlist:
        if item < 0:
            neg_list.append(item)
    if sum(neg_list) == 0:
        print('Отрицательных значений тут нет!')
    else:
        print('Максимальный отрицательный элемент: {}, его индекс: {}.'.format(max(neg_list), intlist.index(max(neg_list))))
    a = sys.getsizeof(intlist)
    count_intlist = sum([sys.getsizeof(item) for item in intlist])
    b = sys.getsizeof(item)
    c = sys.getsizeof(neg_list)
    count_neglist = sum([sys.getsizeof(item) for item in neg_list])

    print('Эта великолепная функция скушала {} байт памяти (включая лист-аргумент)!'.format(a + b + count_intlist + c + count_neglist))

print(max_neg(a))
print(max_neg2(a))
print(max_neg3(a))
