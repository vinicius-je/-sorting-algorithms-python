import random
from bubbleSort import bubbleSort
from insertionSort import insertionSort


def main():
    list = random.sample(range(1, 100), 20)
    print(list)
    insertionSort(list)
    print(list)

if __name__ == '__main__': 
    main()