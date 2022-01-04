import re

my_string="""
hellow world
1223
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Mr. T
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

#This search for Mr with the dot(.) in the name 
pattern=re.compile(r"Mr\.?\s\w+")

#To extract all the  names inluding Mr,Ms and Mrs. Do it like this
pattern2=re.compile(r"(Mr|Ms|Mrs)\.?\s\w+")

#To extract the emails, use this pattern
pattern3=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)")

matches=pattern.finditer(my_string)
matches2=pattern2.finditer(my_string)
matches3=pattern3.finditer(my_string)

for match in matches:
    print(match)
    print("Match2 _________________________")

for matches in matches2:
    print(matches)
    print("Next is emails_________________")

for match3 in matches3:
    print(match3)

