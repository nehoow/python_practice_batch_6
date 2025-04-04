#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
# ill use a loop the iterates every character 
# if the character iscapitalize ill can swap it 
test_string = "wonyouNg aRM"
result = ""
for char in test_string:
    if char.isupper():
        lowercase = char.swapcase()
        result += lowercase
    else:
        result += char
print(result)