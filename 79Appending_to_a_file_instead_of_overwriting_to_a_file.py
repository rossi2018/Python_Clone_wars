with open("78file.txt", mode="a") as my_file:
    text=my_file.write("\nJust added this line using append mode")
    print(text)