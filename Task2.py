import time
import cProfile

N=1000

# Вариант без решета был значительно быстрее поскольку вариант с решетом делает многочисленные вызовы функции, строящей списки простых чисел

# без решета

def primechecker(n) : # проверяет простое ли

    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

def primenumber(i): # находит i-e по счету простое число

    count = 0
    j = 2
    while count != i:
        if primechecker(j) == True:
            count += 1
        j += 1

    return j - 1
# 100 loops, best of 3: 8.6 usec per loop n=10
# 100 loops, best of 3: 36.1 usec per loop n = 20
# 100 loops, best of 3: 230 usec per loop n=100

cProfile.run('primenumber(N)')

# N = 100
#      540    0.000    0.000    0.000    0.000 Task2.py:10(primechecker)
#        1    0.000    0.000    0.000    0.000 Task2.py:28(primenumber)

# N = 1000
    #  7918    0.009    0.000    0.009    0.000 Task2.py:10(primechecker)
    #     1    0.004    0.004    0.013    0.013 Task2.py:28(primenumber)



# с решетом

def sieve(n):

    prime_list = []
    sieve_list = [i for i in range(n+1)]
    for i in range(2,n+1):
        if sieve_list[i] != 0:
            prime_list.append(i)
            for j in range(i*2, n+1, i):
                sieve_list[j] = 0
    return prime_list

def prime_sieve(i):
    n = 2
    while len(sieve(n)) != i:
        n += 1
    a = sieve(n)
    return a[-1]

# 100 loops, best of 3: 162 usec per loop n=10
# 100 loops, best of 3: 904 usec per loop n=20
# 100 loops, best of 3: 43 msec per loop n=100

cProfile.run('prime_sieve(N)')

#N = 100
    #   541    0.033    0.000    0.039    0.000 Task2.py:46(sieve)
    #   541    0.004    0.000    0.004    0.000 Task2.py:49(<listcomp>)
    #     1    0.001    0.001    0.040    0.040 Task2.py:57(prime_sieve)
    #     1    0.000    0.000    0.040    0.040 {built-in method builtins.exec}
    #   540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    # 30167    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}

#N = 1000
#      7919    8.030    0.001    9.279    0.001 Task2.py:51(sieve)
#      7919    0.925    0.000    0.925    0.000 Task2.py:54(<listcomp>)
#         1    0.193    0.193    9.475    9.475 Task2.py:62(prime_sieve)
#         1    0.000    0.000    9.475    9.475 {built-in method builtins.exec}
#      7918    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#   4238087    0.324    0.000    0.324    0.000 {method 'append' of 'list' objects}



