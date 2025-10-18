import random
import sys

def generateInput():
    length = random.randint(200, 500)
    return [random.randint(1, 2000) for _ in range(length)]

def findMean(numbers):
    total = sum(numbers)
    return total / len(numbers)

def findMedian(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2

def main():
    numbers = generateInput()
    print("Mean:", findMean(numbers))
    print("Median:", findMedian(numbers))
    sys.exit()

if __name__ == "__main__":
    main()