import random


def findEvenNumber(numbers):
    ##################################################
    # Make your code
    ##################################################
    for v in numbers:
        if not v % 2:
            yield v


def main():
    numbers = [random.randint(0, 100) for i in range(10)]
    print('Original list', numbers)
    gen = findEvenNumber(numbers)

    for i in gen:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
