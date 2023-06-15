from cImage import *


def grayPixel(oldPixel, array):
    intensitySum = (oldPixel.getRed() + oldPixel.getGreen() + oldPixel.getBLue())
    aveRGB = intensitySum/3
    newPixel = (aveRGB, aveRGB, aveRGB)
    return newPixel


def makeGrayScale(imageFile):
    oldImage = FileImage(imageFile)    # oldImage_rgb = oldImage.convert('RGB')
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    # default rgb set to all 0s
    newIm = np.zeros((width, height, 3), dtype='uint8') # make three dimensional - x, y, rgb
    print(newIm.ndim)
    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            intensitySum = (oldPixel.getRed() + oldPixel.getGreen() + oldPixel.getBlue())
            aveRGB = intensitySum / 3
            newPixel = (aveRGB, aveRGB, aveRGB)
            newIm[row, col, 0] = aveRGB
            newIm[row, col, 1] = aveRGB
            newIm[row, col, 2] = aveRGB
    data = im.fromarray(newIm, 'RGB')
    data.save('GrayButterfly.png')
    data = FileImage('GrayButterfly.png')

    # displaying the new image next to the old one
    myImageWindow = ImageWin("Grayscale", width * 2, height)
    oldImage.draw(myImageWindow)
    data.setPosition(width + 1, 0)
    data.draw(myImageWindow)
    myImageWindow.exitOnClick()


if __name__ == '__main__':
    makeGrayScale('butterfly.gif')



if __name__ == '__main__':
    makeGrayScale('butterfly.gif')