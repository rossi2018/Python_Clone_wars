import re

test_string="123abc456789abc123ABC"

pattern=re.compile(r"abc")
matches=pattern.finditer(test_string)

#Method  to find pattern in a string. match(), search(),findall(),finditer()

#This method can use alongside the above method. group(),start(),end() and span()


for match in matches:
    print(match)

