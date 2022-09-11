from PIL import Image, ImageDraw, ImageFont # <------ these classes help to draw on image

im = Image.open('carrots.jpg') # relative addr
im2 = Image.open(r'C:\Users\ZAID\Pictures\product-3.jpg') 

font = ImageFont.truetype(r'C:\Windows\Fonts\aliee13.ttf', 140)
font2 = ImageFont.truetype(r'C:\Windows\Fonts\aliee13.ttf', 40)

imd = ImageDraw.Draw(im)

imd.text((200,100), 'Carrots', fill=(255,150,0), font=font)
imd.text((700,700),'Rs. 100.00',fill=(0,0,0),font=font2)
im.save('edited_carrot.jpg')



