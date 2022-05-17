# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
celsius = float(input("Enter celsius:\n"))
fahrenheit = celsius * 1.8 + 32
print("That is " + str(fahrenheit) + " degrees in Fahrenheit.")
