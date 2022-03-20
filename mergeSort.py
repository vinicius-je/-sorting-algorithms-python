def mergeSort(list, begin = 0, end = None):
    if end is None:
        end = len(list)
    if(end - begin > 1):
        middle = (end + begin) // 2
        mergeSort(list, begin, middle)
        mergeSort(list, middle, end)
        merge(list, begin, middle, end)
    
def merge(list, begin, middle, end):
    left = list[begin:middle]
    right = list[middle:end]
    i, j = 0, 0
    for k in range(begin, end):
        if i >= len(left):
            list[k] = right[j]
            j += 1
        elif j >= len(right):
            list[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
