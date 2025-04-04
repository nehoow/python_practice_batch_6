#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#Check if all characters are lowercase by iterating and checking for uppercase.
string = "wonyoung pretty"
is_lower = True
for char in string:
    if 'A' <= char <= 'Z':
        is_lower = False
        break
print(is_lower)