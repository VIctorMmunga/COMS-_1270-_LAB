#Vicctor Mmunga
#Date: 10-13-2025

import sys

def get_input():
    numbers = []
    while True:
        user_input = input("Enter a number (or '*' to stop): ")
        if user_input == "*":
            break
        try:
            numbers.append(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    return numbers
def findMin(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value
def findMax(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
def main():
    numbers = get_input()
    if numbers:
        print("Minimum:", findMin(numbers))
        print("Maximum:", findMax(numbers))
    else:
        print("No numbers entered.")
    sys.exit()
if __name__ == "__main__":
    main()