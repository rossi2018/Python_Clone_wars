import re

pattern=re.compile("this") # compile allow us to give a pattern
pattern2=re.compile("search this inside of this text please! ") #use this line to demostrate how to use full match

string="search this inside of this text please! "
string2="search this inside of this text please! Rossi"

a=pattern.search(string)  #this way you can use pattern everyway like this
print(a.group())

b=pattern.findall(string)
print(b)

c=pattern2.fullmatch(string)
print(c) #Fullmatch give exact match here

d=pattern2.match(string2)
print(d)  #match will give you the match of the text and does nit care what come after word

