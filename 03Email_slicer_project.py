#What is slice? A Slice is small thing of something larger
#What is a string? A string is a bunch of letter that are together 
#Note: string are Iterable data type meaning that you can go step by step till you reach the end 

#Get user email assress 
email=input("What is your address?: ").strip()

#Slice out user name 
user=email[:email.index("@")]

#Slice domain name
domain=email[email.index("@")+1:]

#format message 
output="Your user name {} and your domain name is {}".format(user,domain)


#display output message 
print(output)