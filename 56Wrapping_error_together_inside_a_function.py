def sum(num1,num2):
    try:
        return num1/num2
    except (TypeError,ZeroDivisionError ):
        print("Oooops")

print(sum(1,'2'))
print(sum(1,0))