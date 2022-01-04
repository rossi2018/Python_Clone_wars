import re

#There are function  to modify object which are sub and split

#Using the split method
test_string="123abc456789abc123ABC"
pattern=re.compile(r"abc")

splitted=pattern.split(test_string)
print(splitted)

#Using the sub method
test_string2="hello world, you are the best world"
pattern2=re.compile(r"world")
subbed_string=pattern2.sub("Planet",test_string2)
print(subbed_string)


#Combining sub and split
print("Combining____________________________")

urls= """
http://python-engineer.com
https://www.python-engineer.com
http://www.pyeng.net
"""

pattern3=re.compile(r"https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)")
matches=pattern3.finditer(urls)
for match in matches:
    print(match)

subbed_urls=pattern3.sub(r"\2\3 ",urls)
print(subbed_urls)