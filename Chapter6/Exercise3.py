# Encapsulate the code in a function named count and generalize it so that it accepts the string and the letter as arguments.

def count(word, letter):
    counter = 0

    for letters in word:
        if letters == letter:
            counter = counter + 1
    print("There are " + str(counter) + " " + letter + "'s in the word " + word)

count(input("What is your word?\n"), input("What letter would you like to count?\n"))
