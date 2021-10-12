user_name=input("What is your username ? \n")
password=input("Whats your password ? \n")
password_length=len(password)
hidden_password=password_length * "*"

print(f"your user name is: {user_name} and your password {hidden_password} is {password_length} letters long")

