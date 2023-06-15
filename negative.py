from cImage import *
import numpy as np


def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel


def makeNegative(imageFile):
    oldImage = FileImage(imageFile)  # oldImage_rgb = oldImage.convert('RGB')
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    # default rgb set to all 0ss
    newIm = np.zeros((width, height, 3), dtype='uint8')  # make three-dimensional - x, y, rgb
    print(newIm.ndim)
    for row in range(height):
        for col in range(width):
            pixel = oldImage.getPixel(col, row)
            r = 255 - pixel.getRed()
            g = 255 - pixel.getGreen()
            b = 255 - pixel.getBlue()
            newIm[row, col, 0] = r
            newIm[row, col, 1] = g
            newIm[row, col, 2] = b
    data = im.fromarray(newIm, 'RGB')
    data.save('NegativeButterfly.png')
    data = FileImage('NegativeButterfly.png')

    # displaying the new image next to the old one
    myImageWindow = ImageWin("Negative", width * 2, height)
    oldImage.draw(myImageWindow)
    data.setPosition(width + 1, 0)
    data.draw(myImageWindow)
    myImageWindow.exitOnClick()


if __name__ == '__main__':
    makeNegative('butterfly.gif')
