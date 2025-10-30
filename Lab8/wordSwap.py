import random

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    swapped = {}
    
    for word in words:
        swapped[word] = random.choice(words)
    
    print(swapped)
    
    new_sentence = ' '.join([swapped[word] for word in words])
    print(new_sentence)

if __name__ == "__main__":
    main()