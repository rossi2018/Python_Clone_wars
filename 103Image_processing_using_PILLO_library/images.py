from PIL import Image,ImageFilter

img=Image.open("./206_pikachu.jpg")

image_filter=img.convert("L")
resize=image_filter.resize((300,300))
resize.save("blur.png",'png')


