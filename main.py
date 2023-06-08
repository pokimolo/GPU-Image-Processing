from cImage import *

win = ImageWin("cImage Demo", 800, 500)

im = FileImage('castle.gif')

red = Pixel(255, 0, 0)

y = 0
for x in range(im.getWidth()):
    im.setPixel(x, y, red)

for x in range(im.getWidth()):
    for y in range(im.getHeight()):
        pixel = im.getPixel(x, y)
        negative = Pixel(255-pixel.getRed(), 255-pixel.getGreen(), 255-pixel.getBlue())
        im.setPixel(x, y, negative)

im.setPosition(100, 100)
im.draw(win)


win.exitOnClick()