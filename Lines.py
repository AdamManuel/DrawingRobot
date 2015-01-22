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
        self.findDistance()

    def __init__(self, Coordinate1:Coor, Coordinate2:Coor):
        self.Coor1 = Coordinate1
        self.Coor2 = Coordinate2
        self.findDistance()

    def setCoordinate1(self, Coordinate:Coor):
        self.Coor1 = Coordinate
        self.findDistance()

    def setCoordinate2(self, Coordinate:Coor):
        self.Coor2 = Coordinate
        self.findDistance()

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