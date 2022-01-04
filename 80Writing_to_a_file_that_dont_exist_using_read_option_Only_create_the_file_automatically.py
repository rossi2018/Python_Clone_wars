with open("81file.txt", mode="w") as my_file:
    text = my_file.write(
        "This is new .It was created by just writing to the file")
    print(text)

# This demostrate that write create a file if it doesnt exist and it also overwrite the content of a file.
# So if you want to add new content to a file use append 1
