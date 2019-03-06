# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

number = int(input("Сколько компаний будет? "))
QUARTERS = 4

# помню, что в Python 3.7 OrderedDict и dict - одно и то же.
findict = collections.OrderedDict()

for i in range(number):
    findict[input("Введите название компании номер {}: ".format(i+1))] = 0

profits_total = [0 for _ in range(number)]

for j, company in enumerate(findict):
    q_profits = [0, 0, 0, 0]
    for i in range(QUARTERS):
        q_profits[i] = int(input("Для компании {} введите прибыль за {}-й квартал: ".format(company, i+1)))
    findict[company] = q_profits
    profits_total[j] = sum(q_profits)

average = sum(profits_total)/len(profits_total)

below_average = []
above_average = []

for k, company in enumerate(findict):
    if profits_total[k] > average:
        above_average.append(company)
    else:
        below_average.append(company)

print('')
print("Компании с выручкой выше среднего:")
for company in above_average:
    print(company)
print("Компании с выручкой ниже или равной средней:")
for company in below_average:
    print(company)
