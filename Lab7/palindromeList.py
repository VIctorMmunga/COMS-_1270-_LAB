import sys

def get_input():
    words = []
    while True:
        user_input = input("Enter a word (or '*' to stop): ")
        if user_input == "*":
            break
        words.append(user_input)
    return words
def palindromeList(words):
    for i in range(len(words) // 2):
        if words[i] != words[-(i + 1)]:
            return False
    return True
def main():
    words = get_input()
    if palindromeList(words):
        print("The list forms a palindrome.")
    else:
        print("The list does not form a palindrome.")
    sys.exit()
if __name__ == "__main__":
    main()