#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function
#i will iterate every character and check if its uppercase using A to Z  it will return true if it does
test_string = "WONYOUNG"
if not test_string:
    result = False
else:
    result = True
    for char in test_string:
        if 'a' <= char <= 'z':
            result = False
            break
        elif char.isalpha() and not ('A' <= char <= 'Z'):
            result = False
            break
print(f"'{test_string}' is uppercase: {result}")