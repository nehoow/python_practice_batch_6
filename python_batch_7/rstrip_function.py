#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
#Trim trailing spaces from a string by iterating backwards and slicing.
string = "hello wonyoung   "
lastindex = len(string) - 1
while lastindex >= 0 and string[lastindex].isspace():
    lastindex -= 1
result = string[:lastindex + 1]
print(result)