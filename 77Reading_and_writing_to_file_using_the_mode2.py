with open("78file.txt",mode="r+") as my_file:    
    text=my_file.write("Hey it's \nme !")
    print(text)

#When reading and writing at the same, it resets the cursor position and write to the same file. 
# Thereby overwriting the previous text in the files.So be careful when using it