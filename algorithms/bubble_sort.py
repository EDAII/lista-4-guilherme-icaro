import random
import time

def bubble_sort(array):
    fim = len(array)

    while fim  > 0:
        i = 0
        while i < fim-1:
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
            i += 1
        fim -= 1

    return array
#
# i = 0
# while i < 5:
#     array = list(range(0,(10 ** i)))
#     array.sort(reverse=True)
#     # print(array)
#     antes = time.time()
#     bubble_sort(array)
#     depois = time.time()
#     total = (depois - antes)*1000
#     print("%0.5f" %total)
#     array.sort(reverse=True)
#     i += 1
#
# i = 0
# while i < 5:
#     array = list(range(0,(10 ** i)))
#     array.sort()
#     # print(array)
#     antes = time.time()
#     bubble_sort(array)
#     depois = time.time()
#     total = (depois - antes)*1000
#     print("%0.3f" %total)
#     array.sort()
#     i += 1
#
# i = 0
# while i < 5:
#     array = list(range(0,(10 ** i)))
#     random.shuffle(array)
#     # print(array)
#     antes = time.time()
#     bubble_sort(array)
#     depois = time.time()
#     total = (depois - antes)*1000
#     print("%0.3f" %total)
#     random.shuffle(array)
#     i += 1
