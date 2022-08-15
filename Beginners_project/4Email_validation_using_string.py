#Email validation in python using string function 

# A valid email address has four parts:

# 1.Recipient name
# 2.@ symbol
# 3.Domain name
# 4.Top-level domain

# 1. Recipient name
# The recipient name represents an email mailbox that belongs to:

# A specific person
# A mailing list
# A department
# A role within a company (such as sales or customer service)

# 2.Domain name
# The domain name is a string of letters and digits that defines a space on the Internet owned and 
# controlled by a specific mailbox provider or organization.

# 3. Top-level domain
# Top-level domains are the highest level of the domain name system for the Internet and is placed after the domain name in an email address.

# Common top-level domains are:

# .com
# .net
# .org

# Examples of valid email addresses include:

# johndoe@domainsample.com
# john.doe@domainsample.net
# john.doe43@domainsample.co.uk

print("Program to check Valid email address format")

email=input("Enter your email :  " ) #valid email rossi@gmail.com or rossi@gmail.co.uk

#Initialize to check this special characters that are not allowed 
space=0
upper_character=0
hash_mark=0

if len(email)>= 6: # r@g.in(wrong character length of email.Must be 6 and above)
    if email[0].isalpha(): # 1rossi@gmail.com
        if ("@" in email) and (email.count("@")==1): #3 rossi@gmail@gmail.com
            if (email[-4]==".") ^ (email[-3]=="."): #4 rossi@gmail.c wrong email
                for i in email:
                    if i ==i.isspace():  #rs rossi@gmail.com  wrong
                        space=1
                    elif i.isalpha():
                        if i==i.upper():  #Rossi@gmail.com wrong
                            upper_character=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:  #ro#rossi@gmail.com  wrong
                        hash_mark=1 

                if space==1 or upper_character==1 or hash_mark==1:
                    print("Email cant contain space,upper character or hash mark")
                else:
                    print("Right email") 
            else:
                print("The last portion of the email(the domain) must be at least two characters, for example: .com, .org, .cc")
        else:
            print("Email can only contain one(1) @ symbol")
    else:
        print("Email start with letter, not number")
else:
    print("The Email length must be greater than six character")
