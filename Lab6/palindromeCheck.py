import reverseString

def palindromeCheckV1(words) :
    return words == reverseString.reverseStringV1(words)
def palindromeCheckV2(words):
    left, right = 0, len(words) - 1
    while left < right:
        if words[left] != words[right]:
            return False
        left += 1
        right -= 1
    return True
def main():
    word1 = input("Enter a word/phrase for V1 palindrome check: ")
    result1 = palindromeCheckV1(word1)
    print("Is palindrome (V1)?", result1)
    word2 = input("Enter a word/phrase for V2 palindrome check: ")
    result2 = palindromeCheckV2(word2)
    print("Is palindrome (V2)?", result2)
if __name__ == "__main__":
    main()