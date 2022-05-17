# Exercise 2: Write a program that prompts for a list of numbers and at the end prints out both the maximum and minimum of the numbers.

max = float()
min = float()

while True:
    try:
        number = input("Please enter a number (when done, type 'done'): ")
        if number != "done":
            if float(number) > float(max):
                max = number
            if float(number) < float(min):
                min = number
            continue
        if number == "done":
            print("Max: " + str(max))
            print("Min: " + str(min))
            break
    except:
        print("That's not a valid option.")
