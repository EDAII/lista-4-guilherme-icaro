def selection_sort(array):

    length = len(array)

    for i in range(0, length, 1):

        higher = i

        for j in range(i+1, length, 1):
            if array[higher] > array[j]:
                higher = j

        if higher != i:
            tmp = array[higher]
            array[higher] = array[i]
            array[i] = tmp

    return array
