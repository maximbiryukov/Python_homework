# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib

S = 'papa'

def substringer(a, n): # возвращает список с хешами всех подстрок списка a длины n
    output = []
    for i in range(len(a)):
        if(len(a[i:n+i]) == n):
            b = hashlib.sha1(a[i:n+i].encode()).hexdigest()
            if b not in output:
                output.append(b)
    return output

def substring_counter(S): # выводит количество подстрок строки S и список хешей всех уникальных подстрок

    substring_hashes = []

    counter = 0

    for i in range(1, len(S)):
        a = substringer(S, i)
        substring_hashes.append(a)
        counter += len(a)
        print("Количество подстрок длиной {} - {}".format(i, len(a)))

    print("")
    print("Общее количество уникальных подстрок строки \"{}\": {}.".format(S, counter))
    print("")
    print("А вот и хеши всех уникальных подстрок:")
    print("")
    print(substring_hashes)

substring_counter(S)