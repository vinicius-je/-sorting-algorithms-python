def insertionSort(list):
    list_length = len(list)
    for i in range(1, list_length):
        element = list[i]
        j = i - 1
        while j >= 0 and list[j] > element:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = element