from translate import Translator
translator= Translator(to_lang="ja")

try:
    with open("83Folder_app/file.txt",mode="r") as my_file:
        text=my_file.read()
        translation = translator.translate(text)
        with open("83Folder_app/new_file_just_translated", mode="w") as my_file2:
            my_file2.write(translation)


except FileNotFoundError:
    print("File does not exist")
