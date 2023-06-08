from cImage import *
import math
from pixelmapping import *


def convolve(anImage, pixelRow, pixelCol, kernel):
    kernelColumnBase = pixelCol - 1
    kernelRowBase = pixelRow - 1

    rSum = 0
    gSum = 0
    bSum = 0
    for row in range(kernelRowBase, kernelRowBase + 3):
        for col in range(kernelColumnBase, kernelColumnBase + 3):
            kColIndex = col - kernelColumnBase
            kRowIndex = row - kernelRowBase

            aPixel = anImage.getPixel(col, row)
            red = aPixel.getRed()
            green = aPixel.getGreen()
            blue = aPixel.getBlue()

            rSum += red * kernel[kRowIndex][kColIndex]
            gSum += green * kernel[kRowIndex][kColIndex]
            bSum += blue * kernel[kRowIndex][kColIndex]
    if rSum < 0:
        rSum = 0
    if gSum < 0:
        gSum = 0
    if bSum < 0:
        bSum = 0
    if rSum > 255:
        rSum = 255
    if gSum > 255:
        gSum = 255
    if bSum > 255:
        bSum = 255

    newPixel = Pixel(int(rSum), int(gSum), int(bSum))
    return newPixel


def kernel(theImage, mask):
    newIm = EmptyImage(theImage.getWidth(), theImage.getHeight())

    for row in range(1, theImage.getHeight() - 1):
        for col in range(1, theImage.getWidth() - 1):
            newPixel = convolve(theImage, row, col, mask)

            newIm.setPixel(col, row, newPixel)

    return newIm


def makeBlur(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Edge Detection", width * 2, height)
    oldImage.draw(myWin)

    mask1 = [[1/13, 2/13, 1/13], [2/13, 1/13, 2/13], [1/13, 2/13, 1/13]]
    mask2 = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
    blurredImage = kernel(oldImage, mask1)
    sharpenIm = kernel(blurredImage, mask2)
    sharpenIm.setPosition(width + 1, 0)
    sharpenIm.draw(myWin)

    myWin.exitOnClick()

if __name__ == '__main__':
    makeBlur('butterfly.gif')