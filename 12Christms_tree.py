
picture= [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

#iterate over picture
for row in picture:  
    for pixel in row:
        if (pixel==1):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

#Iterate over picture 
#if 0 -> print ""
#if 1 -> print *
