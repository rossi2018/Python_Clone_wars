#Using function , i applied DRY by calling the function several times
picture= [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

def show_tree():
    #iterate over picture
    for row in picture:  
        for pixel in row:
           if (pixel==1):
               print("*",end="")
           else:
               print(" ",end="")
        print("")


show_tree()
print()
show_tree()
print()


    
