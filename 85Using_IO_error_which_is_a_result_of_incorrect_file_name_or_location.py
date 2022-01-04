try:
    with open("83Folder_app/file.txt",mode="r") as my_file:
        print(my_file.read())

except FileNotFoundError as err:
    print("file does not exist")
    raise err

except IOError as err:
    print("IO error")
    raise err