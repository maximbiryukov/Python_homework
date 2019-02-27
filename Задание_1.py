# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

import random

MIN = 2
MAX = 99
SIZE = 10
a = [random.randint(MIN, MAX) for _ in range(SIZE)]

def rationizer(intlist):
    print(intlist)
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    for number in intlist:
        if number % 2 == 0:
            two += 1
        elif number % 3 == 0:
            three += 1
        elif number % 4 == 0:
            four += 1
        elif number % 5 == 0:
            five += 1
        elif number % 6 == 0:
            six += 1
        elif number % 7 == 0:
            seven += 1
        elif number % 8 == 0:
            eight += 1
        elif number % 9 == 0:
            nine += 1
    print('Кратных 2-м: {}, кратных 3-м: {}, кратных 4-м: {}, кратных 5-ти: {}, кратных 6-ти: {}, кратных 7-ми: {}, кратных 8-ми: {}, кратных 9-ти: {}.'.format(two, three, four, five, six, seven, eight, nine))
    return (two + three + four + five + six + seven + eight + nine)

print('Всего кратных любому из чисел в диапазоне от 2 до 9: {} из {} сгенерированных'.format(rationizer(a), SIZE))
