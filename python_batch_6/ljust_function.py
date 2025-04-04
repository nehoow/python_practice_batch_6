#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
# i would print the filler characters until desired length of the difference of desiredlength and the string.
test_string = "wonyoung"
length = 15
fillchar = '~'

if len(test_string) >= length:
    print(test_string)  # No padding needed
else:
    padding_length = length - len(test_string)
    padding = fillchar * padding_length
    print(test_string + padding)