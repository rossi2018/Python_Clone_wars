#Functions are powerful because you use it to organize code in logical blocks because its easier to use and reuse

name="Kay"
number=len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

name="Cameron "
print("Hello " + name + ". Your lucky number is " + str(number))

print("___"* 10)
#can rewrite the above code by using function which make me not repeat myself(DRY)

def lucky_number(name2):
    number2=len(name2) * 9
    print("Hello " + name2 + ". Your lucky number is " + str(number2))

lucky_number("Kay")
lucky_number("Cameron")