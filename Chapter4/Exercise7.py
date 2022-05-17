# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
#  Score      Grade
# >= 0.9        A
# >= 0.8        B
# >= 0.7        C
# >= 0.6        D
#  < 0.6        F

def computepay(score):
    # score = float(input("Please enter a value between 0.0 and 1.0: "))
    
    if score > 1.0 or score < 0.0:
      print("Error, out of range.")
    elif score >= 0.9:
      print("Grade: A")
    elif score >= 0.8:
      print("Grade: B")
    elif score >= 0.7:
      print("Grade: C")
    elif score >= 0.6:
      print("Grade: D")
    else:
      print("Grade: F")

print("Please enter a value between 0.0 and 1.0:")
computepay(float(input()))
