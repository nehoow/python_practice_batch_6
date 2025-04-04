#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
# Iterate through characters, capitalizing the first letter of each word (after a non-alphabetic character) and lowercasing the rest, 
# using isalpha(), upper(), and lower().
test_string = "woNYOUNG aRM 123"
result = ""
capitalize_next = True
for char in test_string:
    if char.isalpha():
        if capitalize_next:
            result += char.upper()
        else:
            result += char.lower()
        capitalize_next = False
    else:
        result += char
        capitalize_next = True
print(f"'{test_string}' titled: '{result}'")