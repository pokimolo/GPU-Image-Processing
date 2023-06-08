from cImage import *


def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel


def makeNegative(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Negative Image", width * 2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newPixel = negativePixel(oldPixel)
            newIm.setPixel(col, row, newPixel)

    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()

if __name__ == '__main__':
    makeNegative('butterfly.gif')
