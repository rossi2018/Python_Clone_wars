#Anagrams are words formed by rearranging the letters of another word, For example, car and arc, cat and act, etc.
#The problem asks us to return the list of anagrams together in one big array. We can then return with 
# list(table.values()) in python which would return all the values of our table in a list of arrays with anagrams.

def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(groupAnagrams(words))