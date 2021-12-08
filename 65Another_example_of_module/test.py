import utility
#you can write the above code like this 
from utility import multiply,divide

import shopping.more_shopping.shopping_cart 
#you can write the abovecode in a simpler way like this
from shopping.more_shopping.shopping_cart import buy
#or write it this way to avoid name collision 
from shopping.more_shopping import shopping_cart

print(utility.divide(2,3))

print(divide(5,2))
print(multiply(5,2))

print(shopping_cart.buy("Apple laptop"))
print(shopping.more_shopping.shopping_cart.buy("apple"))
print(buy("allpe juice"))

if __name__=="__main__":
    print("Checking if this is the main file")