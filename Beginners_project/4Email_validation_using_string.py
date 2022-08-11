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

email=input("Enter your email :  " ) #,rossi@gmail.com
k,j,d=0,0,0
if len(email)>= 6: # r@g.in(wrong character length of email.Must be 6 and above)
    if email[0].isalpha(): # 1rossi@gmail.com
        if ("@" in email) and (email.count("@")==1): #3 rossi@gmail@gmail.com
            if (email[-4]==".") ^ (email[-3]=="."): #4 rossi@gmail.c wrong email
                for i in email:
                    if i ==i.isspace(): #5 #rs rossi@gmail.com
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): #W-- W==W  #5 #Rossi@gmail.com
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:  #5 ws#rossi@gmail.com
                        d=1 

                if k==1 or j==1 or d==1:
                    print("Email can't contain  space and Upper Character")
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
