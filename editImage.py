from PIL import Image, ImageDraw, ImageFont 
from main import IM_newRow, IM_oldRow, IM_changeRow
def thoudsandSep(num4thoudsand):
    num4thoudsand = f'{int(num4thoudsand):,}'
    return num4thoudsand
fontSize = 46

image = Image.open('template.jpeg')

draw = ImageDraw.Draw(image)
#219x and 208x apart 
#60y apart 
#first base text at 498,260
x = [498,717,925]
y = [260,322,383,445,505,570,635]

for i in range(7):
    draw.text(xy=(x[0],y[i]),text=(IM_newRow[i]),fill=(0,0,0),font=ImageFont.truetype('arialbd.ttf',fontSize),anchor='mm')
    draw.text(xy=(x[1],y[i]),text=(IM_oldRow[i]),fill=(0,0,0),font=ImageFont.truetype('arialbd.ttf',fontSize),anchor='mm')
    draw.text(xy=(x[2],y[i]),text=(IM_changeRow[i]),fill=(0,0,0),font=ImageFont.truetype('arialbd.ttf',fontSize),anchor='mm')
        

draw.text(xy=(925,125),text=("มีผลบังคับใช้วันที่ 14 ก.ค. 2565"),fill=(0,0,0),font=ImageFont.truetype('cordia.ttc',36),anchor='mm',stroke_width =1)



image = image.save('C:\\Users\\VPS\\Desktop\\IM_Image\\edited.jpeg')




