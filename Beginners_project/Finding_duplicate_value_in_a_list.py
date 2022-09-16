

def find_uniqe(myList):         
    uniques=[]
    dups=[]
    for each in myList:
        if each not in uniques:
            uniques.append(each)
        else:
            dups.append(each)

    return dups

print(find_uniqe(["James", "Calvin Harris", "Jennifer", "James", 
         "Calvin Harris", "Michael Jackson", "Dj snake"]))


def find_unique2(items):
    duplicats=[]
    for i in items:
        if items.count(i)>1 and i not in duplicats:
            duplicats.append(i)
    return duplicats

print(find_unique2(["James", "Calvin Harris", "Jennifer", "James", 
         "Calvin Harris", "Michael Jackson", "Dj snake"]))
