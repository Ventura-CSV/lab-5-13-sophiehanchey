import random


def findEvenNumber(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    numbers = [random.randint(0, 100) for i in range(10)]
    print('Original list', numbers)
    gen = findEvenNumber(numbers)

    for i in gen:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
