# function to read the names from the input file.
def readFile():
    file = open("inputs/problem22.txt", "r")
    names = file.read().split(",")
    file.close()

    return names

# this function will return a new list of names sorted in alphabetical order.
def sortNames(names):
    sortedNames = sorted(names)
    return sortedNames

# this function will return the value of a word. The value of a word is the sum of the values of its letters.
def wordValue(word):
    word = word.strip('"')
    value = 0
    for letter in word:
        value += ord(letter) - 64

    return value

# main function
def main():
    names = readFile()
    sortedNames = sortNames(names)
    total = 0
    for i in range(len(sortedNames)):
        total += (i + 1) * wordValue(sortedNames[i])

    print(total)

main()


