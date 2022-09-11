from PIL import Image, ImageFilter, ImageEnhance # <--------- 2 classes added

im = Image.open('carrots.jpg') # relative addr
im2 = Image.open(r'C:\Users\ZAID\Pictures\product-3.jpg') 

# im2.filter(ImageFilter.EMBOSS).show()
# im2.filter(ImageFilter.CONTOUR).show()
# im2.filter(ImageFilter.FIND_EDGES).show()
# im2.filter(ImageFilter.BLUR).show()
# im2.filter(ImageFilter.SHARPEN).show()
# im2.filter(ImageFilter.SMOOTH).show()
# im2.filter(ImageFilter.MaxFilter(3)).show()  # highlight whites
# im2.filter(ImageFilter.MinFilter(3)).show()  # highiight blacks
# im2.filter(ImageFilter.MedianFilter(5)).show() # hightlight greys
# im2.filter(ImageFilter.GaussianBlur(40)).save('peas_blurred.jpg')

# eim = ImageEnhance.Color(im)
# for i in range(-10,11,2):
#     eim.enhance(i).show()

imc = im.copy()
im2_s = im2.resize((300,240))
imc.paste(im2_s, (0,0))
imc.paste(im2_s, (700,0))
imc.show()
