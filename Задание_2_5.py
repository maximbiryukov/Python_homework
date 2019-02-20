# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

START = 32
END = 127
step = 10
while (START <= END):
    for j in range(step):
        if ((START + j) > END):
            break
        print ('{}-{} '.format(START + j, chr(START + j)), end = '')
    print("")
    START += step
