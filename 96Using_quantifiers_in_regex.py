import re

# Quantifier:

# *:0 or more
# +:1 or more
# ?:0 or 1, -> optional character
# {4}: exact number
# {4,6}: range numbers (min,max)

dates = """
hello
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11

2020/04/02

2020_04_04
2020_04_04
"""

pattern = re.compile(r"\d\d\d\d[-/]\d\d[-/]\d\d")

#When you are looking for specific month 
pattern2=re.compile(r"\d{4}[-/]0[56][-/]\d\d")

matches = pattern.finditer(dates)
matches2=pattern2.finditer(dates)

for match in matches:
    print(match)
    print("second iteration------------------")
    

for match1 in matches2:
    print(match1)

