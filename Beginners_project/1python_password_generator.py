import random,string


#create password generator
#1.specify the length of password characters like 3 for letters,2 for digits
#2.Ask the user to input the length of the of password
#3.Iterate through the length using the range
#4.write a function that converts the password string to list,then applying shuffle.Let it return string using the join method. 
#The essence of shuffle is to make the password appear in no specific order
#5.print out the password using the function 

number_of_digits=3
number_of_punctuation_character=2


number_of_passwords=int(input("How many password do you want to generate? "))
password_length=int(input("Provide the password length: "))

for password_index in range(number_of_passwords):
    password=""

    for digits_index in range(number_of_digits):
        password=password+random.choice(string.digits)

    for punctuation_index in range(number_of_punctuation_character):
        password=password+random.choice(string.punctuation)

    for index in range(password_length - number_of_digits - number_of_punctuation_character):
        password=password+random.choice(string.ascii_letters)

    def randomize_password(password):
        password_list = list(password)
        random.shuffle(password_list)
        return "".join(password_list)
        

    print(password_index +1,randomize_password(password))

