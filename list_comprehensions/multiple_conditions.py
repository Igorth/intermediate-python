# Strings that start with "a" and end in "y"
options = ["any", "albany", "apple", "world", "hello", ""]
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue
    if string[0] != "a":
        continue
    if string[-1] != "y":
        continue

    valid_strings.append(string)

print(valid_strings)


valid_strings = [
    string 
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
    ]
print(valid_strings)