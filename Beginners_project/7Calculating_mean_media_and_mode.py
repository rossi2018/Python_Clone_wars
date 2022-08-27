#Mean Median and Mode using Python

#mean
list1 = [13,14,15,16,2,2,45,67]
mean = sum(list1)/len(list1)
print(mean)

#Median
#The Median is the middle value among all the values in sorted order
# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}th term

list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)


#mode 
#Mode is the most frequently occurring value among all the values
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)