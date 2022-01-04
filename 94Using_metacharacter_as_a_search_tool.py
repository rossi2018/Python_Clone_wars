import re

test_string="123abc456789abc123ABC"
pattern=re.compile(r".")
pattern2=re.compile(r"ABC$")

#All meta characters: . ^ $ * + ? { } [ ] \ | ( )
# > Any character (except newline character)
# ^ starts wwith (E.g "^ hello")
# $ Ends with "world$"
# * zero or more occurence  (e.g " aix*")
# + one or more occurrences (e.g "aix+")
# { } Exactly the specified number of occurences (e.g "al{2}")
# [ ] a set of characters  (e.g" [a-m]")
# \ special sequence (or escape special characters ) (e.g "\d" )
# | Either (e.g "falls|stays")
# () capture and group

matches=pattern.findall(test_string)

for match in matches:
    print(match)
print("_________________________________")
match2=pattern2.search(test_string)
print(match2)