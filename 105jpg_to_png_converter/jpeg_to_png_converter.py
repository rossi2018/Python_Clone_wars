import sys
import os
from PIL import Image

# grab first and second argurment
image_folder=sys.argv[1]
output_folder=sys.argv[2]



#check is  new/ exists, if not create new
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through the image folder 
for filename in os.listdir(image_folder):
    img=Image.open(f"{image_folder}{filename}")
    #When we grabe the image we need to save it as dot png(.png) discarding dot jpg(.jpg)
    clean_name=os.path.splitext(filename)[0]
    # print(clean_name)

    #then conver images to png  and save to the new folder
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("all done! ")


#to ru this script ,use this pattern below (note that you will need to have a folder that contain the image)
# $python3 jpeg_to_png_converter.py images/ new/
#Note new/ directory is a folder that will be created to contain the new converted file to .png 
#While images/ directory contain the images in .jpg that needs converting
    



