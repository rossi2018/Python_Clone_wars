multiples=[]
for x in range(1,11):
    multiples.append(x * 7)

print(multiples)

#List comprehsions: Let us create new list based on sequences or ranges 
multiples2=[ x * 7 for x in range(1,11)] 
print(multiples2)