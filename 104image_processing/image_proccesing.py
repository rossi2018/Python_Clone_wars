from PIL import Image,ImageFilter

img=Image.open("./bitcoin.jpg")
img.thumbnail((400,400))
img.save("thumbnail.jpg")

print(img.size)