# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

fname = input("Enter your file name: ")
fhand = open(fname)
count = 0
floatTotal = 0

for line in fhand:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence:') == -1: continue
    count = count + 1
    floatLine = float(line[20:])
    floatTotal = floatTotal + floatLine
print("There are", count, "lines total.")
print("The total of the float values are:", floatTotal)
print("The average spam confidence is:", floatTotal/count)
