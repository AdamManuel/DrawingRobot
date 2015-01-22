__author__ = 'Adam Manuel'
from PIL import Image, ImageFilter, ImageOps
from Lines import Lines
from Coordinate import Coor


#Creates an outline of the picture
def getEdges(picture:Image, Threshold:int):
        #splits image into two colors based on darkness of pixels
        #Credit to "cur4so" on Stack Overflow
        mask=picture.convert("L")
        mask = mask.point(lambda i: i < Threshold and 255)
        #Uses edge detector from ImageFilter in Pillow
        picture = mask.filter((ImageFilter.FIND_EDGES))
        picture = ImageOps.invert(picture)
        return picture

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
