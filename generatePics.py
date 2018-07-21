#coding:utf-8

#生成图片


from PIL import Image, ImageFont, ImageDraw,ImageColor


#创建一张纯色图片，包含一个标准圆和边界标志
def createPic(size, color):
	image = Image.new('RGB', size, color)
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf",30)

	r = min(*size) / 2
	halfMaxL = max(*size) /2
	#线的像素宽
	width = 5
	text = "{}X{}".format(size[0],size[1])

	#画圆
	if size[0] > size[1]:
		draw.ellipse((halfMaxL - r +2,2, halfMaxL + r -2,size[1] -2),fill="white")
	else:
		draw.ellipse((2, halfMaxL - r+2,size[0] -2,halfMaxL + r-2),fill="white")

	#画一个比白色圆半径小width宽度的内圆，颜色和图片底色相同
	if size[0] > size[1]:
		draw.ellipse((halfMaxL - r +width,width, halfMaxL + r -width,size[1] -width),fill=color)
	else:
		draw.ellipse((width, halfMaxL - r+width,size[0] -width,halfMaxL + r-width),fill=color)

	#尺寸文字
	draw.text([size[0]/2 - 50,size[1]/2 -10],text,align="center",fill="white",font=font)
	#左上边界文字
	draw.text([2,2],"border",fill="white",font=font)
	#右下文字
	draw.text([size[0]-90,size[1]-30],"border",align="right",fill="white",font=font)
	#image.show()
	image.save('D:\\Files' + '\\' + text + '.jpg')

createPic((900,100),"brown")

