from PIL import Image

im = Image.open('carrots.jpg') # relative addr
im2 = Image.open(r'C:\Users\ZAID\Pictures\product-3.jpg') # absolute addr

print(im)
print(im2)

im.rotate(45).show()
im2.rotate(90).show()