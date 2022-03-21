import random
# from bubbleSort import bubbleSort
# from insertionSort import insertionSort
# from mergeSort import mergeSort
from quickSort import quickSort

def main():
    list = random.sample(range(1, 100), 20)
    print(list)
    quickSort(list, 0, len(list) - 1)
    print(list)

if __name__ == '__main__': 
    main()