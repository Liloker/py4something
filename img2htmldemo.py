# -*- coding: utf-8 -*-
# Nola
"""
img2html : Convert image to HTML

optional arguments:
  -b #RRGGBB, --background #RRGGBB  background color (#RRGGBB format)
  -s (4~30), --size (4~30)          font size (int)
  -c CHAR, --char CHAR              characters
  -t TITLE, --title TITLE           html title
  -f FONT, --font FONT              html font
  -i IN, --in IN                    要转换的图片
  -o OUT, --out OUT                 输出文件名
$ img2html -i before.jpg -o before_html.html
"""
from img2html.converter import Img2HTMLConverter

converter = Img2HTMLConverter(char='LoveKarin', title='亲爱的karin')
html = converter.convert('2.png')
with open('2.html', mode='w', encoding='utf-8') as f:
    f.write(html)