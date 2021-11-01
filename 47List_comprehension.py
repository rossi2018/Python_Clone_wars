#list comprehensio 

my_list=[]

for char in "hello":
    my_list.append(char)

print(my_list)

#the short way to write thi =s code using list comprehension is 

my_list2=[char for char in "hello"]
print(my_list2)

my_list3=[num for num in range(1,101)]
print(my_list3)

my_list4=[num*2 for num in range(1,101)]
print(my_list4)

#to generate the list of even number from 1 to 100 in the power of 2 

print("__" * 6)
my_list5=[num **2 for num in range(1,101) if num% 2 ==0]
print(my_list5)