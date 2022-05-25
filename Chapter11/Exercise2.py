"""
Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.

Enter file:mbox.txt
38549
Enter file:mbox-short.txt
39756
"""

import re

fname = input("Enter a file name: ")
fhand = open(fname)
listOfNums = list()
added = 0
count = 0

for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision:\s([0-9]+)', line)
    if x:
        num = x[0]
        count += 1
        listOfNums.append(num)
    else:
        continue

for number in listOfNums:
    added += int(number)
    average = added / count

print(int(average))
