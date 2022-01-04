import re

email_search_pattern = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = "rossi@gmail.com"
email2 = "rossi.com"

a = email_search_pattern.search(email)
b = email_search_pattern.search(email2)
print(a)
print(b)
