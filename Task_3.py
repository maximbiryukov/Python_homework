import random

LIST_LEN = 2 * random.randint(1, 100) + 1

lizt = [random.randint(-10, 15) for i in range(LIST_LEN)]


def median_finder(intlist):

    print(intlist)
    dict1 = {}
    for number in lizt:
        dict1[number] = [0, 0]

    for key, value in dict1.items():
        for number in lizt:
            if key == number:
                continue
            elif key > number:
                value[0] += 1
            else:
                value[1] += 1

    #print(dict1)

    medianz = lizt[0]
    min_spread = dict1[lizt[0]][0] - dict1[lizt[0]][1]
    for key in dict1:
        for number in lizt:
            if abs(dict1[number][0] - dict1[number][1]) < abs(min_spread):
                min_spread = dict1[number][0] - dict1[number][1]
                medianz = number

    print("Медиана этого списка: {}".format(medianz))

    return medianz

print("Вот список: ")
median_finder(lizt)




