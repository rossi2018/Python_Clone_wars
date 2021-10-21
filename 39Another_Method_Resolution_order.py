class X:pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

#you can use the dunder method with mro or just mro to check for the order of inheritance
print(M.__mro__)