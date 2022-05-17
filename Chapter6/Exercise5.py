# Exercise 5: Take the following python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# use find and string slicing to extract the portion of the string after the colon character 
# and then use the float function to convert the extracted string into a floating point number

str = 'X-DSPAM-Confidence:0.8475'
findColon = str.find(':') # index 18
sliced = str[18 + 1:]
floated = float(sliced)
print(type(floated))
