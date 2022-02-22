from changePosition import changePosition

def bubbleSort(list):
    list_length = len(list)
    # runs the code n-1 times to sort the list
    for i in range(list_length - 1):
        # runs the element list n-1 each execution (n-1), to change element position
        for j in range(list_length - 1):
            if list[j] > list[j+1]:
                changePosition(list, j+1, j)