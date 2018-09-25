import random
import time

def insertion_sort(array):
    i = 1
    while i < len(array):
        temp = array[i]
        change = False
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            change = True
            j -= 1
        if change:
            array[j+1] = temp
        i += 1

    return array

#
# i = 0
# while i < 5:
#     array = list(range(0,(10 ** i)))
#     array.sort(reverse=True)
#     # print(array)
#     antes = time.time()
#     insertion_sort(array)
#     depois = time.time()
#     total = (depois - antes)*1000
#     print("%0.5f" %total)
#     array.sort(reverse=True)
#     i += 1
# i = 0
# while i < 5:
#     array = list(range(0,(10 ** i)))
#     array.sort()
#     # print(array)
#     antes = time.time()
#     insertion_sort(array)
#     depois = time.time()
#     total = (depois - antes)*1000
#     print("%0.3f" %total)
#     array.sort()
#     i += 1
