import random
from bubbleSort import bubbleSort


def main():
    list = random.sample(range(1, 100), 20)
    print(list)
    bubbleSort(list)
    print(list)

if __name__ == '__main__':
    main()