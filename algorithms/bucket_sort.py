from algorithms.shell_sort import shell_sort
import random
import time

def bucket_sort(array):
    largest = max(array)
    length = len(array)
    size = largest/length

    buckets = [[] for _ in range(length)]

    for i in range(length):
        j = int((array[i]/size))
        if j != length:
            buckets[j].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    for i in range(length):
        shell_sort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


# array = list(range(0,(10)))
# random.shuffle(array)
# print(array)
# antes = time.time()
# array = bucket_sort(array)
# depois = time.time()
# total = (depois - antes)*1000
# print(array)
# print("%0.3f" %total)
