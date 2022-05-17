# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40.

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
  
