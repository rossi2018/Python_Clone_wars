#MRO - Method Resolution Order

#        A
#     /      \
#    /        \
#    B        C
#    \        /
#     \      /
#         B



class A:
    num=10

class B(A):
    pass

class C(A):
    num=1

class D(B,C):
    pass

print(D.num)

#This will print out the MRO of the class 
print(D.mro())