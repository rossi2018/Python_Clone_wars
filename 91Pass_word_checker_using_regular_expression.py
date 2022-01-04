import re

#The regular expression should have this pattern
#At least 8 characters long
#Contain any sort of letters, number and symbols $%#@
#Has to end with a number

password_pattern=re.compile(r"(^[A-Za-z0-9$%#@]{8,}\d)")

password="JamesMathisoiininiasii#001"
password2="Thisisit"

check_password=password_pattern.fullmatch(password)
check_password2=password_pattern.fullmatch(password2)
print(check_password)
print(check_password2)