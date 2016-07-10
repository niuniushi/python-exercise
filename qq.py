import Image
import ImageDraw
import ImageFont
im=Image.open('qq.jpg')
dr=ImageDraw.Draw(im)
font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf",30)
dr.text((220,20),'2',(255,0,0),font)
im.save('qq1.jpg')
print im.mode
