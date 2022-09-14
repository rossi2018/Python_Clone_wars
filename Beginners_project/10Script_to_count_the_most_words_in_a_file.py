from collections import Counter


#Python Program to Count Most Frequent Words in a File


words=[]
with open("sample.txt","r") as f:
    for line in f:
        words.extend(line.split())

counts=Counter(words)
top5=counts.most_common(5)
print(top5)