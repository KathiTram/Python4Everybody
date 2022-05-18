# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in uppercase.

fname = input("Enter the file name: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip().upper()
    print(line)
