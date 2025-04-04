#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
# i will check if test_string is long enough to contain the suffix and if it is, i will check the trailing portion of the test_string if it matches the suffix.
test_string = "wonyoung.mp4"
suffix = ".mp4"

string_length = len(test_string)
suffix_length = len(suffix)

if string_length >= suffix_length and test_string[string_length - suffix_length:] == suffix:
    result = True
else:
    result = False

print(f"'{test_string}' ends with '{suffix}': {result}")