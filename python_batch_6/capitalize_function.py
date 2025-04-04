#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
#Capitalize the first character and lowercase the rest of the string using upper() and lower().
test_string = "woNYOUNG aRM 123"
if test_string:
    result = test_string[0].upper() + test_string[1:].lower()
else:
    result = ""
print(f"'{test_string}' capitalized: '{result}'")