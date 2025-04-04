#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#Check if a string starts with a specific prefix by comparing the beginning slices.
string = "hellowonyoung"
prefix = "hello"
is_startswith = len(prefix) <= len(string) and string[:len(prefix)] == prefix
print(is_startswith)