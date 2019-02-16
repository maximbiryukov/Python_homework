# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

import math

x = int(input("Provide 3 digit number: "))
huns = math.floor(x/100)
tens = (math.floor(x%100/10))
ones = (math.floor(x%100%10))

total = huns + tens + ones
product = huns * tens * ones

print(total)
print(product)