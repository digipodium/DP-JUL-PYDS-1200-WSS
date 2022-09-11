from PIL import Image

im = Image.open('carrots.jpg') # relative addr
im2 = Image.open(r'C:\Users\ZAID\Pictures\product-3.jpg') # absolute addr

print('resolution',im.size)
print('height', im.height)
print('width',im.width)
print('mode', im.mode)
print('format', im.format)
print('exif', im.info)

im.convert('L').show()
im.resize((100,100)).show()
# im.resize((2000,2000)).show()
im.resize((im.width * 5, im.height * 5)).save('carrots_5x.jpg')
