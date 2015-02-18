__author__ = 'Adam Manuel'
import math


class Coor(object):
    """"This is a class used to store and manipulate coordinates to be used for the machinery"""""
    #X coordinate
    Coorx = None
    #Y coordinate
    Coory = None

    #initalization without data
    def __init__(self):
        Coorx = 0
        Coory = 0

    #initalization with data
    def __init__(self, X, Y):
        self.Coorx = X
        self.Coory = Y

    #gets X
    def getX(self):
        return self.Coorx

    #gets Y
    def getY(self):
        return self.Coory

    #sets X
    def setX(self, X: int):
        self.Coorx = X

    #sets Y
    def setY(self, Y: int):
        self.Coory = Y

    #Finds the distance to another point using distance formula
    def getDistance(self, Other):
        x = math.fabs(self.Coorx - Other.getX())**2
        y = math.fabs(self.Coory - Other.getY())**2
        return (math.sqrt(x + y))

    def toString(self):
        return "("+str(self.Coorx)+" ,"+str(self.Coory)+")"