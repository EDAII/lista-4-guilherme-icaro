import random
import time

def shell_sort(array):
    h = len(array) // 2
    a = 0
    while h > 0:
        i = h
        while i < len(array):
            temp = array[i]
            change = False
            j = i - h
            while j >= 0 and array[j] > temp:
                array[j+h] = array[j]
                change = True
                j -= h
            if change:
                array[j+h] = temp
            i += 1
        h = h // 2
        a += 1

    return array

# i = 0
# while i < 5:
#     array = list(range(0,(10 ** i)))
#     array.sort(reverse=True)
#     # print(array)
#     antes = time.time()
#     shell_sort(array)
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
#     shell_sort(array)
#     depois = time.time()
#     total = (depois - antes)*1000
#     print("%0.3f" %total)
#     array.sort()
#     i += 1
