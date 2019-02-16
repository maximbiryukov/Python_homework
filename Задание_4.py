# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import random

start_int = int(input("Int lower bound: "))
end_int = int(input("Int higher bound: "))
start_float = input("Float lower bound: ")
end_float = input("Float higher bound: ")
start_char = input("Char lower bound: ")
end_char = input("Char higher bound: ")

out_int = random.randint(start_int, end_int)
float_helper = random.random()
out_float = float_helper * float(start_float) + (1 - float_helper) * float(end_float)
out_char = chr(random.randint(ord(start_char), ord(end_char)))

print("Случайное целое число в заданном диапазоне: :%r" % (out_int))
print("Случайное вещественное число в заданном диапазоне: :%r" % (out_float))
print("Случайный символ в заданном диапазоне: :%r" % (out_char))
