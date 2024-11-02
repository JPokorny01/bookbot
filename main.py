def main():
    bookPath = "books/frankenstein.txt"
    wordCount(bookPath)
    charCount(bookPath)


def wordCount(bp):
    with open(bp) as f:
        file_contents = f.read()
        words = file_contents.split()
        wordCount = len(words)
    print(f"Number of words is {wordCount}")

def charCount(bp):
    charDict = dict()
    with open(bp) as f:
        file_contents = f.read()
        for char in file_contents.lower():
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1
    #print(f"Character count is {charDict}")
    print("Character count is:")
    #print(charDict)
    for i in charDict:
        print(f"Character '{i}' was found {charDict[i]} times")        


if __name__ == "__main__":
    main()