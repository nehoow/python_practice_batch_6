#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#Find the last index of a substring by iterating backwards and comparing slices, breaking on first match.
string = "wonyoung is teasing me again i kinda like it"
substring = "like"
last_index = -1
for index in range(len(string) - len(substring), -1, -1):
    if string[index:index + len(substring)] == substring:
        last_index = index
        break
print(last_index)