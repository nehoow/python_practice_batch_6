﻿#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
# Right-justify the string with spaces by adding leading spaces based on width given.
string = "haewon"
width = 10
result = " " * (width - len(string)) + string
print(result)