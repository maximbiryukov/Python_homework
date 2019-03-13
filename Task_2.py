import random
import collections
import cProfile

LIST_LEN = 100
MIN_NUM = 0
MAX_NUM = 49

def merge_zort(intlist):

    split = len(intlist)//2

    if len(intlist) > 1:

        left = intlist[:split]
        right = intlist[split:]

        merge_zort(left)
        merge_zort(right)

        left_index = 0
        right_index = 0
        intlist_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                intlist[intlist_index] = left[left_index]
                left_index += 1
            else:
                intlist[intlist_index] = right[right_index]
                right_index += 1
            intlist_index += 1

        while left_index < len(left):
            intlist[intlist_index] = left[left_index]
            intlist_index += 1
            left_index += 1

        while right_index < len(right):
            intlist[intlist_index] = right[right_index]
            intlist_index += 1
            right_index += 1

lizt = [random.randint(MIN_NUM, MAX_NUM) for i in range(LIST_LEN)]

print("Merge sort:")
print("Ввод:")
print(lizt)
merge_zort(lizt)
print("Вывод: ")
print(lizt)
print("")

cProfile.run('merge_zort(lizt)')