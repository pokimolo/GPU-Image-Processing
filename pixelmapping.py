from cImage import *
from grayscale import *
from negative import *
import numpy as np
from kernel import *
from PIL import Image
from numpy import asarray

def pixelMapper(fileImage, rgbFunction):
    im = Image.open("butterfly.png")
    img = np.array(im)
    width = img.shape[1]
    height = img.shape[0]
    RGB = np.array(2)
    newIm = np.zeros([height, width, RGB])

    for row in range(height):
        for col in range(width):
            oldPixel = img[0, 0]  # Access the x y of the pixel
            newPixel = rgbFunction(oldPixel)  # Access the rgb value of the pixel
            newIm.fill(newPixel)  # Add new values to new array

    return newIm


def generalTransform(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Grayscale", width * 2, height)
    oldImage.draw(myImageWindow)

    newImage = pixelMapper(oldImage, grayPixel)

    newImage.setPosition(oldImage.getWidth() + 1, 0)
    newImage.draw(myImageWindow)
    myImageWindow.exitOnClick()


def channelSplit(image):
    return np.dsplit(image, image.shape[-1])


if __name__ == '__main__':
    '''
    image = Image.open("castle.gif")
    im = image.convert('RGB')
    img = asarray(im)

    height = img.shape[0]
    width = img.shape[1]
    rgb = img.shape[2]

    r = img[:, :, [0]]
    g = img[:, :, [1]]
    b = img[:, :, [2]]

    print(img.size)
    print(img.shape)
    i = 0
    n = 0
    while i <= height:      # row, goes through pixel in row before moving to next
        while n <= width:   # column length used to iterate through row
            print(i, n)
            n = n + 1       # is there a way to speed this up with diter?
        i = i + 1
        n = 0'''




    generalTransform("butterfly.png")

    # Here is where I test all the manipulative functions!
    # I've been able to import the other codes
    # and from there I can determine what works and what doesn't
    # with minimal trial and error across multiple files
