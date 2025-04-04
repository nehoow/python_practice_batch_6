#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
#add leading zeros to reach target width by calculating needed zeros
string = "123"
width = 5
result = "0" * (width - len(string)) + string
print(result)