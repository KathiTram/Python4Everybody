# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

fruit = "banana"
length = len(fruit)
index = 0

while length > index:
    letter = length - 1
    print(fruit[letter])
    length = length - 1
