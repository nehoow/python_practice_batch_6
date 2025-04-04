#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
#Remove a specific suffix if it exists by checking the end and slicing if it matches.
string = "wonyoungarm"
suffix = "arm"
if string.endswith(suffix):
    result = string[:-len(suffix)]
else:
    result = string
print(result)