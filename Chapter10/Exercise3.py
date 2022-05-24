"""
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""

fname = input("Enter a file name: ")
fhand = open(fname)
newText = ''
counts = dict()

for line in fhand:
    line = line.rstrip()
    line = line.lower()
    for letter in line:
        if letter.isalnum():
            newText += letter

for char in newText:
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1

lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
