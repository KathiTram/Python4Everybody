# Exercise 4: List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
# Create a list of unique words, which will contain the final result.
# Write a program to open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in the list of unique words.
# If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words in alphabetical order.

fname = input("Enter file: ")
fhand = open(fname)
uniqueWords = []

for line in fhand:
    t = list(line.split())
    # print(t)

    for word in t:
        # print(word)
        if word not in uniqueWords:
            uniqueWords.append(word)

for each in sorted(uniqueWords):
    print(each)
# print(sorted(uniqueWords))
