import random


def findEvenNumber(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def main():
    numbers = [random.randint(0, 100) for i in range(10)]
    print('Original list', numbers)
    gen = findEvenNumber(numbers)

    for i in gen:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
