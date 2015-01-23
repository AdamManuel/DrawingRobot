__author__ = 'Adam Manuel'
from PIL import Image, ImageFilter, ImageOps
from Lines import Lines
from Coordinate import Coor


#Creates an outline of the picture
def getEdges(picture:Image, Threshold:int):
        #splits image into two colors based on darkness of pixels
        mask=picture.convert("L")
        mask = mask.point(lambda pixel: pixel < Threshold and 255)
        #Uses edge detector from ImageFilter in Pillow
        picture = mask.filter((ImageFilter.FIND_EDGES))
        picture = ImageOps.invert(picture)
        return picture

#Need to make this more efficient
def mergePicture(image1:Image, image2:Image):
    rgb_image1 = image1.convert("RGB")
    rgb_image2 = image2.convert("RGB")
    pixelData1 = image1.load()
    pixelData2 = image2.load()
    sizex = image1.size[0]
    sizey = image1.size[1]
    print("about to merge")
    for x in range(sizex):
        for y in range(sizey):
            pixelRGB = rgb_image1.getpixel((x,y))
            R,G,B = pixelRGB
            if(sum([R,G,B])/3 < 200):
                pixelData2[x,y] = pixelData1[x,y]
    return image2
#TODO Goes line by line in image finding straight lines to use for date
#Creates the info to draw lines
''''
def getLineCoors(picture:Image):
    Data = []
    firstCoor = Coor(0,0)
    secondCoor = Coor(0,0)
    linetoadd = Lines(firstCoor, secondCoor)
    for y in range(len(picture)):
        isBlack = (picture[y][0] == (0,0,0))
        for x in range(len(picture[0])):
            secondCoor = Coor(x,y)
            if(picture[firstCoor.getX()][firstCoor.getY()] != picture[firstCoor.getX()][secondCoor.getY()]):
                '''''
