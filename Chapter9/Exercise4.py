"""
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""

fname = input("Enter a file name: ")
fhand = open(fname)
dictionaryOfEmails = dict()


for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        t = list(line.split())
        dictionaryOfEmails[t[1]] = dictionaryOfEmails.get(t[1],0) + 1

max_value = max(dictionaryOfEmails.values())

max_key = max(dictionaryOfEmails, key=dictionaryOfEmails.get)

print(max_key, max_value)
