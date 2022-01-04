import re

# More special characters:

#\d : Matches any decimal digit; [0-9]
#\d: Matches any non-digit character;
#\s: Matches any whitespace character; (space " " tab "\t" newline "\n")
#\S: Matches any non-whitespace character;
#\w:Matches any alphumeric (word) character; [a-zA-Z0-9_].
#\W:Matches any non-alphanumeric character;
#\b:Matches where the specified character are at the beginning or at the end of a word (r"\bain",r"ain\b")
#\B: Matches wher the special characters are present, but NOT at the begining( or at the end ) of a word (r"\Bain",r"ain\B")


test_string="hello 123_ heyho hohey"

pattern=re.compile(r"[0-4]")
matches=pattern.finditer(test_string)

for match in matches:
    print(match)

