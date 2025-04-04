#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
#Find the first index of a substring by iterating and comparing slices, breaking on first match.
string = "wonyoung smells so nice"
substring = "smell"
index_found = -1
for index in range(len(string) - len(substring) + 1):
    if string[index:index + len(substring)] == substring:
        index_found = index
        break
print(index_found)