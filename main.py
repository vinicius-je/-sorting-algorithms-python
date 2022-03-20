import random
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from mergeSort import mergeSort


def main():
    list = random.sample(range(1, 100), 20)
    print(list)
    mergeSort(list)
    print(list)

if __name__ == '__main__': 
    main()