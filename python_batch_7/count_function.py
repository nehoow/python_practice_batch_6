#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
#I will count the occurrences of a substring by iterating and comparing slices.
string = "wonyoung is so pretty like she is so pretty"
substring = "pretty"
count = 0
for index in range(len(string) - len(substring) + 1):
    if string[index:index + len(substring)] == substring:
        count += 1
print(count)