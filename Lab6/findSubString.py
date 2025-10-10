def findSubStringV1(words,  sub_str ):
    return words.find(sub_str)

def findSubStringV2(words, sub_str):
    if sub_str in words:
        return words.index(sub_str)
    else:
        return -1
def findSubStringV3(words, sub_str):
    for i in range(len(words) - len(sub_str) + 1):
        if words[i:i+len(sub_str)] == sub_str:
            return i
    return -1
def main():
    words2 = input("Enter the main string: ")
    sub_str = input("Enter the substring: ")
    print("Index:", findSubStringV1(words2, sub_str))
    print("Index :", findSubStringV2(words2, sub_str))
    print("Index:", findSubStringV3(words2, sub_str))
if __name__ == "__main__":
    main()