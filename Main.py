__author__ = 'Adam Manuel'

import ImageProcess
from tkinter import Tk
from tkinter import filedialog
from PIL import Image, ImageEnhance
from Lines import Lines
from Coordinate import Coor

#Creates Tkinter window
root = Tk()
root.withdraw()

#Hides the main window
root.withdraw()

#Asks for file
ImagePath = filedialog.askopenfilename()
OriginalPicture = Image.open(ImagePath, "r")

#---Process Image---
picture = OriginalPicture

#Adds a higher contrast
enhancer = ImageEnhance.Contrast(picture)
picture = enhancer.enhance(2)

#outlines the light and dark regions of the picture
picture75 = ImageProcess.getEdges(picture, 50)
picture225 = ImageProcess.getEdges(picture, 205)

#combines the two outlines into one image
pictureAll = ImageProcess.mergePicture(picture75, picture225)

print(ImageProcess.printData(ImageProcess.getLineCoors(pictureAll)))
