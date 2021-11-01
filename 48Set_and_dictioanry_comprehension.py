#set compresion is same thing as list compression,the only differnece is using curly braket {}
#Remeber set only allow unique item and no duplicae is found in set 

my_list2={char for char in "hello"}
print(my_list2)

my_list3={num for num in range(1,101)}
print(my_list3)

my_list4={num*2 for num in range(1,101)}
print(my_list4)

#to generate the list of even number from 1 to 100 in the power of 2 

print("__" * 6)
my_list5={num **2 for num in range(1,101) if num% 2 ==0}
print(my_list5)

#Dictioanry compression
print("==" * 25)
simple_dict={
    "a":1,
    "b":2
}

my_dict={key:value**2 for key,value in simple_dict.items()}
print(my_dict)

my_dict6={key:value**2 for key,value in simple_dict.items() if value%2==0 }
print(my_dict6)

my_dict7={num:num*2 for num in [1,2,3,4,5]}
print(my_dict7)