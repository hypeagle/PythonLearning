#-*- coding:utf-8 -*-

# please pip install pillow
from PIL import Image, ImageFont, ImageDraw

# text = u'春水初生.春林初盛.春风十里 不如你'
text = u'东风袅袅泛崇光，香雾空蒙月转廊。.只恐夜深花睡去，故烧高烛照红妆。'
text_arr = text.split(".")
print text_arr

font = ImageFont.truetype("simkai.ttf", 24)
lines = []

line_width = 0
for word in text_arr:
      print word
      for line in word.split(","):
            if font.getsize(line)[0] > line_width:
                  line_width = font.getsize(word)[0]
            lines.append(line)

padding = 5
gap = 10

img_width = line_width + (padding << 1)
line_height = font.getsize(text)[1]
img_height = line_height * (len(lines)) + gap * (len(lines) - 1) + (padding << 1)

print 'len=', len(lines)
print 'lines=', lines

im = Image.new("RGB", (img_width, img_height), (255, 255, 255))
dr = ImageDraw.Draw(im)

y = padding
for line in lines:
      x = padding + ((line_width - font.getsize(line)[0]) >> 1)
      dr.text((x, y), line, font=font, fill="#000000")

      y += line_height + gap

# im.save("1.png")
im.save("2.png")