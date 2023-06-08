import math
from cImage import *
import numpy as np
from numpy import asarray


def grayPixel(oldPixel):
    intensitySum = (oldPixel[:, :, [0]] ** 2) + (oldPixel[:, :, [1]] ** 2) + (oldPixel[:, :, [2]] ** 2)
    aveRGB = int(math.sqrt(intensitySum / 3))
    pixel = [aveRGB, aveRGB, aveRGB]
    newPixel = [oldPixel.height, oldPixel.width, pixel]

    return newPixel


def makeGrayScale(imageFile):
    oldimage = imageFile.convert('RGB')
    oldimage = asarray(imageFile)
    height = oldimage.shape[0]
    width = oldimage.shape[1]
    rgb = oldimage.shape[2]

    win = ImageWin("Grayscale", width * 2, height)
    imageFile.draw(win)
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newPixel = grayPixel(oldPixel)
            newIm.setPixel(col, row, newPixel)

    newIm.setPosition(width + 1, 0)
    newIm.draw(win)

    win.exitOnClick()


if __name__ == '__main__':
    makeGrayScale('butterfly.gif')
