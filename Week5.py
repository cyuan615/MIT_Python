##############################
# define class
##############################
# class Classname(object):
#     <define attributes here>
import math

class Coordinate(object):
    # this class define a coordinate with x any y attribue
    def __init__(self,x,y):
        self.x = x
        self.y = y
#    def distance(self,other):
#        # calculate self distance with another coordinate
#        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y)**2)


class Plot(object):
    def __init__(self, name):
        self.name=name

    def distance(self, one, another):
        return math.sqrt((one.x - another.x) ** 2 + (one.y - another.y)**2)


point1 = Coordinate(3,4)
point2 = Coordinate(1,3)
# print("calculating distance...")
# print(point1.distance(point2))
# print(point2.distance(point1))

plot1 = Plot('Chang的坐标系')
print(plot1.distance(point1,point2))