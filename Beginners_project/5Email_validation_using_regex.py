# a-z   ^[a-z]   rotali.realme@gmail.com or rotali@gmail.com
# 0-9    
# ._ time 1  [\._]?
# @ time 1   [@]?
# . 2,3  [a-z]{2,3}$

import re 
email_condition= "^[a-z]+[\._]?[a-z 0-9]+[@]?\w+[.][a-z]{2,3}$"
user_email=input("Enter your Email :")

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")