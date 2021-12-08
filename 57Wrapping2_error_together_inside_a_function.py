def sum(num1,num2):
    try:
        return num1/num2
    except (TypeError,ZeroDivisionError ) as err:
        print(err)

print(sum(1,'2'))
print(sum(1,0))