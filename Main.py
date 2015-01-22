__author__ = 'Adam Manuel'

import ImageProcess
from tkinter import Tk
from tkinter import filedialog
from PIL import Image

#Creates Tkinter window
root = Tk()

#Hides the main window
root.withdraw()

#Asks for file
ImagePath = filedialog.askopenfilename()
Origpicture = Image.open(ImagePath, "r")

#TODO Create a GUI that displays preview and lets you choose the threshold using a slider

#Asks about threshold
Origpicture.show()
print("What threshold do you want")
print("(Value between 0-255)")
print("(Lower number to outline darker object and higher number to outline lighter objects)?")
Threshold = int(input())

#Process Image
picture = Origpicture
picture = ImageProcess.getEdges(picture, Threshold)
picture.show()
