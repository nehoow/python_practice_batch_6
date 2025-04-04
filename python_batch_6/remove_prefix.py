#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
#ill use .startswith() to know if the prefix is there
#if the prefix ill use the len of the prefix and starts the index there to "remove" it
input_string = "wonyoung"
prefix = "won"

if input_string.startswith(prefix):
    result = input_string[len(prefix):]
else:
    result = input_string

print(f"Original string: {input_string}")
print(f"Result: {result}")