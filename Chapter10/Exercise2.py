"""
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.py

Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

fname = input("Enter file name: ")
fhand = open(fname)
counts = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        time = line[5]
        timeSplit = time.split(":")
        hours = timeSplit[0]
        if hours not in counts:
            counts[hours] = 1
        else:
            counts[hours] += 1

lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)

