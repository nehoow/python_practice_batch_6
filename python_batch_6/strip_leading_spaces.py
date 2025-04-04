#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
#loop each character of the string, if character is space the loop will continue until it isnt a space then it will return the index number.
#print result using the  index we got from the loop and use it as a starting point, where there are no leading spaces.
test_string = "        wonyoung"
index = 0
while index < len(test_string) and test_string[index].isspace():
    index += 1
print(test_string[index:])