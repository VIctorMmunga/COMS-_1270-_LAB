def reverseStringV1(words1):
    return words1[::-1]

def reverseStringV2(words2):
    return "".join(reversed(words2))

def reverseStringV3( words3):
    reversed_word= " "
    for ch in range(len(words3)-1, -1, -1):
        reversed_word += words3[ch]
    return reversed_word
def reverseStringV4(words4):
    reversed_wor=" "
    for i in words4:
        reversed_wor = i + reversed_wor
    return reversed_wor

def reverseStringV5(words5):
     reversed_wr=" "
     i= len(words5)-1
    
     while i >= 0:
      reversed_wr +=words5[i]
      i-=1
     return reversed_wr
def main():
    words1 = input("Enter your (word) or (phrase): ")
    Answer= reverseStringV1(words1)
    print("Reverse (words) or (phrase):", Answer)
    words2 = input("Enter your words: ")
    Answer2= "".join(reverseStringV2(words2))
    print("Enter Your (words )or (phase): ", Answer2)
    words3 = input("Enter your words: ")
    Answer3= reverseStringV3(words3)
    print("your reversed words:", Answer3)
    words4= input('Enter your words:')
    answer4= reverseStringV4(words4)
    print("your words:",answer4 )
    words5= input("Enter your words: ")
    answer5= reverseStringV5(words5)
    print("Your reversed words: ", answer5)
     
if __name__=="__main__":
     main()