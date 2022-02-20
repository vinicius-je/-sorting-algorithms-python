from algorithms import selectionSort
import random

def main():
    list = random.sample(range(1, 100), 20)
    print('before selection sort')
    print(list)
    selectionSort(list)
    print('after selectio sort')
    print(list)

if __name__ == '__main__':
    main()