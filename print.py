import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

# 使うフォント，サイズ，描くテキストの設定
ttfontname = "C:\\Windows\\Fonts\\meiryob.ttc"
fontsize = 36
text = "暗黙の型宣言"

keys = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetSmall = 'abcdefghijklmnopqrstuvwxyz'

with open('output') as f:
    #print(f.readlines()[1:][0])
    
    for line in f.readlines()[1:]:
        key = line[0]
        index = 0
        for c in line:
            if c == '0':
                index += 1
            if c == '1':
                break
        print(index)
        for i in range(len(keys)):
            keys[i] = keys[i].replace(alphabet[index], key)
            
    print(keys)
    for i in range(len(keys)):
        for j in range(26):
            keys[i] = keys[i].replace(alphabetSmall[j], alphabet[j])

# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (760, 230)
backgroundRGB = (11, 22, 33)
textRGB       = (0, 0, 0)

img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
draw = PIL.ImageDraw.Draw(img)

font = PIL.ImageFont.truetype(ttfontname, fontsize)
textWidth, textHeight = draw.textsize(text,font=font)

def create_image(pos, message, fontColor):
    W, H = pos
    draw = PIL.ImageDraw.Draw(img)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    
    #rect_d.rectangle([W-(w/2), H-(h/2), W+(w/2), H+(h/2)], outline=(255,0,0), width=1)    
    draw.text((W-(w/2), H-(h/2)), message, font=font, fill=fontColor)

s = 76
p = 4
for y in range(3):
    for x in range(len(keys[y])):
        pos = ((x+y/2) * s, y*s)
        rect_d = PIL.ImageDraw.Draw(img)
        rect_d.rectangle([(x+y/2) * s+p, y*s+p, (x+y/2+1) * s-p, (y+1)*s-p], fill=(64, 64, 64), outline=(255, 255, 255), width=4)
        
        create_image(((x+y/2+1/2) * s, (y+1/2)*s-4), keys[y][x], (255, 255, 255))
        #draw.text((x*s+s + y*s, y*s+s), keys[y][x], fill=(255, 255, 255), font=font)


img.show()

img.save("image.png")