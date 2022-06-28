from math import pi

def cirle(r):
    return pi*(r **2)
    

radii=[12,34,56,777,8,999,00]

for r in radii:
    print(cirle(r))
    

print("_______________")

import numpy as np

np.random.seed(122245)
yes=np.random.randint(1,4)
print(yes)