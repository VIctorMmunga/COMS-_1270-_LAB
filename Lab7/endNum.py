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
def endNum(numbers, num):
    result=[]
    end=[]
    for x in numbers:
        if x== num:
            end.append(x)
        else:
            result.append(x)
    return result + end
def main():
    numbers = get_input()
    num = int(input("Enter the number to move to the end: "))
    print("Previous list:", numbers)
    print("Updated list:", endNum(numbers, num))
    sys.exit()
if __name__ == "__main__":
    main()