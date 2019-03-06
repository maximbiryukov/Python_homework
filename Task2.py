# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections

a = input("Введите первое HEX число: ")
b = input("Введите второе HEX число: ")

c = []
d = []

for char in a:
    c.append(char)

for char in b:
    d.append(char)

def hex_to_dec(list):
    hexdict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    output = 0
    for i in range(1,len(list)+1):
        output += hexdict[list[i-1]] * 16**(len(list)-i)
    return output

def dec_to_hex(number):
    hexdict = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6','7':'7', '8':'8', '9':'9', '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    hex_out = collections.deque()
    quotient = number // 16
    remainder = number % 16
    hex_out.append(hexdict[str(remainder)])
    while quotient != 0:
        remainder = quotient % 16
        quotient = quotient // 16
        hex_out.appendleft(hexdict[str(remainder)])
    return hex_out

dec_total = hex_to_dec(c) + hex_to_dec(d)
dec_product = hex_to_dec(c) * hex_to_dec(d)

print("Их сумма: ", end='')
print(dec_to_hex(dec_total))
print('')
print("Их произведение: ", end='')
print(dec_to_hex(dec_product))