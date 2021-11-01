def count_letter(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter]= 0
        result[letter] += 1
    return result

print(count_letter("aaaaa"))
print(count_letter("Rossi"))
print(count_letter("tenant"))
print(count_letter("a long string with a lot of letters"))

#This technique can be used in alot of cases like counting how many times error appeared in the log your analyze 