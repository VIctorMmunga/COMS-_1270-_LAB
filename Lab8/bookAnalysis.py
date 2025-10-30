# Your Name
# Date: YYYY-MM-DD
# Lab #: X
# Description: Analyzes a text file, counts words, and outputs a sorted list of word counts.

def analyzeBook(filename):
    count = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                # Remove punctuation
                word = word.replace('_','').replace('"','').replace(',','').replace('.','')
                word = word.replace('-','').replace('?','').replace('!','').replace("'","")
                word = word.replace('(','').replace(')','').replace(':','').replace('[','')
                word = word.replace(']','').replace(';','')
                word = word.lower()
                if word.isalpha():
                    count[word] = count.get(word, 0) + 1
    return count

def outputAnalysis(counts, filename):
    keys = list(counts.keys())
    keys.sort()
    output_filename = filename.replace('.txt', '_analysis.txt')
    with open(output_filename, 'w', encoding='utf-8') as f:
        for word in keys:
            f.write(f"{word} {counts[word]}\n")
    print(f"Analysis saved as {output_filename}")

def main():
    filename = input("Enter your book filename: ")
    counts = analyzeBook(filename)
    outputAnalysis(counts, filename)

if __name__ == "__main__":
    main()
