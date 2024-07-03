import random


def findEvenNumber(numbers):
    evenNums = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            evenNums.append(numbers[i])
        
    return evenNums


def main():
    numbers = [random.randint(0, 100) for i in range(10)]
    print('Original list', numbers)
    gen = findEvenNumber(numbers)

    for i in gen:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
