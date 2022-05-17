# Exercise 3: Write a program to prompt the user for hours and rate per hour to computer gross pay.
hours = int(input("Hours: "))
rate = float(input("Rate: "))
pay = hours * rate
print("Pay: " + str(pay))
