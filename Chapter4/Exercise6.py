# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
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

print("Enter your hours and rate:\n")
computepay(int(input()), float(input()))
