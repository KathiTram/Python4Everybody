# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

try:
  hours = int(input("Hours: "))
  rate = float(input("Rate: "))

  if hours > 40:
    overtimeHours = hours - 40
    overtimePay = overtimeHours * 1.5 * rate
    regularPay = 40 * rate
    totalPay = overtimePay + regularPay
    print("Your overtime pay is: " + str(overtimePay))
    print("Your regular pay is: " + str(regularPay))
    print("Your total pay is: " + str(totalPay))
  else:
    pay = hours * rate
    print("Your pay is: " + str(pay))
except:
  print("Error, please enter a numeric input")
