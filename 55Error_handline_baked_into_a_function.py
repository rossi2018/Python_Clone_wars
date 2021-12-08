def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers {err} ")

print(sum(1,'12'))