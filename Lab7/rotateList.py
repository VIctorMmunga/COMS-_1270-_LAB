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
def rotateList(numbers, rot):
    rot = rot % len(numbers)  # To handle rotations larger than list length
    return numbers[-rot:] + numbers[:-rot]
def main():
    numbers = get_input()
    rot = int(input("Enter the number of positions to rotate: "))
    print("Rotated list:", rotateList(numbers, rot))
    sys.exit()
if __name__ == "__main__":
    main()