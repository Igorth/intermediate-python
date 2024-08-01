# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", mode="w") as file:
    file.write("This is a new file.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# mode="a" -> append to the end of the file
with open("my_file.txt", mode="a") as file:
    file.write("\nThis is a new line.")

# Absolut path is coming from the root directory
# Relative path is coming from the current working directory
