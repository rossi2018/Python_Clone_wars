# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

x=lambda a : a + 10

print(x(4))

# Lambda functions can take any number of arguments:
x2 = lambda a, b : a * b
print(x2(25, 6))

x3 = lambda a, b, c : a + b + c
print(x3(5, 6, 2))

