import re

# in regular expression this means something
pattern = re.compile(r"([a-zA-Z]).([a])")
# you can think of regular expression as an entire language on itself with different pattern that you use to find
# pattern inside a text

# side not: r before the qoute means raw string, the next close bracket is group 1 followed by the next closed bracket
# which is group two. The dot between the two groups indicate anything in regular expression

# the whole world of regular expression is complicted. As a programmer i dont expect you to learn all of them

# To make things easy by testing  regular expression outside your code, use this website https://regex101.com/https:/
# It allows you to create your Regular Expression outside of your code. Paste an example of the test text you will be
#  searching, and start typing in your expression at the top. Regex101 will update live with an explanation of any
# special characters in your pattern as well as highlighting the matches in your test string.

string = "search this inside of the text please! Andrei"

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.group())
print(a.group(1))
print(a.group(2))


# If you want to spend a few hours learning about RegEx in detail and want to follow  a fun interactive tutorial, here
# is a nice free way to get yourself confortable with some of the common pattern. Go to this website
# https://regexone.com/
