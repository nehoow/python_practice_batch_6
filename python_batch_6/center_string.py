#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
#i will calculate left and right padding to evenly distribute space around the string to center it within the specified length, and print the resulting padded string.
test_string = "wonyoung"
length = 20
fillchar = ' '

string_length = len(test_string)

if string_length >= length:
    print(test_string)  # No padding needed
else:
    padding_length = length - string_length
    left_padding = padding_length // 2
    right_padding = padding_length - left_padding
    padding = fillchar * left_padding + test_string + fillchar * right_padding
    print(padding)