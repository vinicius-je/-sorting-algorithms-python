def changePosition(list, p1, p2):
    aux = list[p2]
    list[p2] = list[p1]
    list[p1] = aux

def selectionSort(list):
    list_length = len(list)
    for i in range(list_length - 1):
        min_index = i
        # find the lowest value index
        for j in range(i, list_length):
            if list[j] < list[min_index]:
                min_index = j
        if list[i] > list[min_index]:
            changePosition(list, i, min_index)


