a="helloooooooooo"

if (n := len(a)) > 10:
    print(f" the length is {n}")

while ((n := len(a)) > 1):
    print(n)
    a=a[:-1]
print(a)
