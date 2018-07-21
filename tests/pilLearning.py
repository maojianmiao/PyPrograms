#coding:utf-8

#PIL Learning
#maojm
#
from PIL import Image
from PIL import PSDraw
 
im = Image.open("lena.ppm")
title = "lena"
box = (1*72, 2*72, 7*72, 10*72) # in points
 
ps = PSDraw.PSDraw() # default is sys.stdout
ps.begin_document(title)
 
# draw the image (75 dpi)
ps.image(box, im, 75)
ps.rectangle(box)
 
# draw centered title
ps.setfont("HelveticaNarrow-Bold", 36)
w, h, b = ps.textsize(title)
ps.text((4*72-w/2, 1*72-h), title)
 
ps.end_document()
imagePath = r"C:\testres"
deadpool = imagePath + '\\' + 'deadpool.jpg'
img = Image.open(deadpool)
#img.show()
#逆时针旋转45度，并用系统自带工具展现
#img.rotate(45).show()
#
#创建缩略图
#img.thumbnail((100,100), Image.ANTIALIAS)
#img.save(imagePath + "\\deadpool.thumbnail","JPEG")

#imgnew = Image.eval(img,lambda i:i*3)
#imgnew.show()

out = img.point(lambda i:i * 1.2)
source = out.split()
source[0].point(lambda i:255)
source[1].point(lambda i:0)
source[2].point(lambda i:0)
im = Image.merge("RGB",source)
im.show()
print im.mode


 
