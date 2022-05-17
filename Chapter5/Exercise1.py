# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
total = 0
count = 0

while True:
    done = input("Please enter a number (when done, type 'done'): ")
    try:
        if done != "done":
            total = total + float(done)
            count = count + 1
            continue
        if done == "done":
            average = total / count
            print("Total: " + str(total))
            print("Count: " + str(count))
            print("Average: " + str(average))
            break
    except:
        print("That's not a number.")
