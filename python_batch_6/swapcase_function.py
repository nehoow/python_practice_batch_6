#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
#Iterate through each character, converting lowercase to uppercase and vice versa using isupper(), lower(), and upper().
test_string = "woNYOUNG aRM 123"
result = ""
for char in test_string:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char
print(f"'{test_string}' swapcased: '{result}'")