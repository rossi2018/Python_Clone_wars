import re

#The compilation flags are listed below
#ASCII, A: Makes several escapes like \w \b  and \d match only ASCII characters
#DOTALL, S: Make. match any character, including newlines.
#IGNORECASE, I : Do case-insensitive matches
#LOCALE, L: Do a locale-aware match.
#MULTILINE, M : Multi-line matching, affecting ^ and $.
#VERBOSE, X (for 'extended'): Enable verbose REs, which can be organized more cleanly and understandably.

my_string="Hello World"
pattern=re.compile(r"world",re.I)
matches=pattern.finditer(my_string)

for match in matches:
    print(match)