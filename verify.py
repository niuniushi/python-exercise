import Image
import ImageDraw
import ImageFont
import ImageFilter
import random

im=Image.new('RGB',(300,100),'white')
dr=ImageDraw.Draw(im)
fo=ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf",30)



for i in range(4):
    dr.text((60*(i+1),35),chr(random.randint(65,90)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),fo)

for ii in range(random.randint(1500,3000)):
        dr.point((random.randint(0,300),random.randint(0,100)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

im=im.filter(ImageFilter.BLUR)

im.save('verify code.jpg')

