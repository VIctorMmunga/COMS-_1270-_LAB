# Victor Mmunga
# Date: 10 -27-2025
# Lab #: 08
# Description: Reads a text file, removes all non-ASCII characters, and writes the cleaned content to a new file.

def readFile(testFile.txt):
    with open("testFile.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def removeNonASCII(text):
    clean = ""
    for char in text:
        if ord(char) < 128:  
            clean += char
    return clean
def writeFile(content, original_filename):
    new_filename = original_filename.replace('.txt', '_clean.txt')
    with open(new_filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned file saved as {new_filename}")

def main():
    filename = input("Enter the filename: ")
    content = readFile(filename)
    cleaned = removeNonASCII(content)
    writeFile(cleaned, filename)

if __name__ == "__main__":
    main()
