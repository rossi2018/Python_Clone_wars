# Regular expression: A regular expression is a special sequence of characters that helps you match or find other
#  strings or sets of strings, using a specialized syntax held in a pattern

# Reguar expression is used in validaion checking, checking if password matches requirement,want to check if a piece
# of string exist in a piece of text

# python come with a regular expression module call re

import re

string = "search inside of this text please!"

a = re.search("this", string)
print(a)

#To use other feaatures of regular expression 
print(a.span()) #this will show the start and stop index number of the string

print(a.start()) #this will show only the start index number

print(a.end()) #it will show the end of the index number

print(a.group()) #this will return the part of the string where they was a match>Group is useful when you are trying to do multiple searches

