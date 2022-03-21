def quickSort(list, low_limit, high_limit):
    if low_limit < high_limit:
        pivot = partition(list, low_limit, high_limit)
        quickSort(list, low_limit, pivot - 1)
        quickSort(list, pivot + 1, high_limit)

def partition(list, low, high):
    pivot = list[low]
    i = low + 1
    j = high

    while i <= j:
        while i <= j and list[i] <= pivot: 
            i += 1
        while j >= j and list[j] > pivot: 
            j -= 1
        if i < j: 
            list[i], list[j] = list[j], list[i]
    list[low], list[j] = list[j], list[low]
    return j