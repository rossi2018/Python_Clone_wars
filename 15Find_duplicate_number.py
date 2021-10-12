some_list=["a","b","c","b","d","m","n","n"]

dumplictes=[]
for value in some_list:
    if some_list.count(value)>1:
        if value not in dumplictes:
            dumplictes.append(value)
    
print(dumplictes)






