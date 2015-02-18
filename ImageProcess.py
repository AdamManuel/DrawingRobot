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

#splits image into two colors based on darkness of pixels
def getOnlyBWImage(picture: Image, Threshold:int):
    mask=picture.convert("L")
    mask = mask.point(lambda pixel: pixel < Threshold and 255)
    return mask.convert("RGB")

#turns the image in to a grayscale image
def getBWImage(picture:Image):
    return picture.convert("LA")

#TODO Need to make this more efficient
def mergePicture(image1:Image, image2:Image):
    rgb_image1 = image1.convert("RGB")
    pixelData1 = image1.load()
    pixelData2 = image2.load()
    for x in range(image1.size[0]):
        for y in range(image1.size[1]):
            R,G,B = rgb_image1.getpixel((x,y))
            if(sum([R,G,B])/3 < 200):
                pixelData2[x,y] = pixelData1[x,y]
    print("Merging Done")
    return image2

#TODO FINISH THIS DAMN METHOD
def getLineCoors(picture:Image):
    #use .getpixel on rgb_image and add the line to the Data array
    Data = []
    rgb_image = picture.convert("RGB")

    return Data

def printData(Data):
    for x in range(len(Data)):
        print((Data[x]).toString())