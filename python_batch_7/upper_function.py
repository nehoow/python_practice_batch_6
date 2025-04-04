#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
#Convert all characters to uppercase by iterating and converting lowercase using swapcase
string = "HellO wonYounG"
result = ""
for char in string:
    if char.islower():
        result += char.swapcase()
    else:
        result += char
print(result)
