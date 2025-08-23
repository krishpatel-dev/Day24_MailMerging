with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("my_file.txt", "a") as file:
#     file.write("\nMy favourite color is yellow")

with open("my_file2.txt", "w") as file2:
    file2.write("hyy there!")