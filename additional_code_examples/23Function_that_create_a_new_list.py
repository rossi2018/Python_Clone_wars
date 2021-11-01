def full_emails(people):
    result=[]
    for email,name in people:
       result.append("{} <{}>".format(name,email)) 
    return  result 

print(full_emails([("rossi12@gmail.com","Alex Church"),("ray211@gmail.com","Ray Jay")]))