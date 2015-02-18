__author__ = 'Adam Manuel'
from Coordinate import Coor



class Lines(object):

    Coor1 = None
    Coor2 = None
    PenDown = False
    Distance = None

    def __init__(self):
        self.Coor1 = Coor(0,0)
        self.Coor2 = Coor(0,0)
        self.PenDown = False
        #self.findDistance()


    def __init__(self, Coordinate1:Coor, Coordinate2:Coor, isPen:bool):
        self.Coor1 = Coordinate1
        self.Coor2 = Coordinate2
        #self.findDistance()
        self.PenDown = isPen


    def setCoordinate1(self, Coordinate:Coor):
        self.Coor1 = Coordinate
        #self.findDistance()

    def setCoordinate2(self, Coordinate:Coor):
        self.Coor2 = Coordinate
        #self.findDistance()

    def getCoordinate1(self):
        return self.Coor1

    def getCoordinate2(self):
        return self.Coor2

    def setPen(self, isPen:bool):
        self.PenDown = isPen

    def isPenDown(self):
        return self.PenDown

    def findDistance(self):
        self.Distance = Coor(self.Coor1).getDistance(self.Coor2)

    def getDistance(self):
        return self.Distance

    def toString(self):
        toReturn = ""
        toReturn += "Coordinate 1: "+ self.Coor1.toString() + "\n"
        toReturn += "Coordinate 2: "+ self.Coor2.toString() + "\n"
        toReturn += "Is pen down? " + str(self.isPenDown()) + "\n"
        return toReturn