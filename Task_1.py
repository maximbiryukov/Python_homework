import random

LIST_LEN = 100
MIN_NUM = -100
MAX_NUM = 99

def bubble_zort(intlist):

    last_item = len(intlist)
    sorted = False
    counter = 0
    swaps = 0
    while not sorted:
        counter += 1
        sorted = True
        for i in range(last_item - 1):
            if intlist[i] > intlist[i + 1]:
                swaps += 1
                intlist[i], intlist[i + 1] = intlist[i + 1], intlist[i]
                sorted = False
        last_item -= 1

    return counter, swaps

a = [random.randint(MIN_NUM, MAX_NUM) for i in range(LIST_LEN)]

print("Bubble sort:")
print("Ввод:")
print(a)
bubble_zort(a)
print("Вывод: ")
print(a)
print("")


# код для тестирования эффективности

TEST_NUM = 10000
measurements = []
for i in range(TEST_NUM):
    measurements.append(bubble_zort([random.randint(MIN_NUM, MAX_NUM) for i in range(LIST_LEN)]))

runs = 0
swaps = 0

for measure in measurements:
    runs += measure[0]
    swaps += measure[1]

print("Среднее (на сортировку) количество \"пробегов\" после {} тестов со списками длиной в {} элементов (n): {}".format(TEST_NUM, LIST_LEN, runs/TEST_NUM))
print("Среднее (на сортировку) количество замен после {} тестов со списками длиной в {} элементов (n): {}".format(TEST_NUM, LIST_LEN, swaps/TEST_NUM))




