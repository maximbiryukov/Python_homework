# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

def numfind(n):
    if n == 1:
        return 1
    else:
        return (-0.5)**(n-1)

n = int(input("Введите количество элементов: "))

sum = 0
for i in range(n):
    sum += numfind(i+1)

print(sum)

