##############################
# define class
##############################
# class Classname(object): Chang's example
#     <define attributes here>
'''
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

# MIT example:
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
    def __sub__(self,other):
        return Coordinate(self.x - other.x,self.y - other.y)

c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.distance(origin)) # = print(Coordinate.distance(c,origin))
print(type(c))

# use isinstance() to check if an object is a Coordinate
print(isinstance(c,Coordinate))
print(c.__str__())
print(c.__sub__(origin))

########################################
# Classes Examples
########################################
class fraction(object):
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self,other):
        numerNew = other.getDenom() * self.getNumer() + self.getDenom() * other.getNumer()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew,denomNew)       ########## ??????????????? fraction
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() - self.getDenom() * other.getNumer()
        denomNew = other.getDenom() * self.getDenom()
        return numerNew / denomNew
    def convert(self):
        return self.getNumer() / self.getDenom()


oneHalf = fraction(1,2)
twoThird = fraction(2,3)
new = oneHalf + twoThird
sub = oneHalf - twoThird

print(oneHalf)
print(oneHalf.getNumer()) # = print(fraction.getNumer(oneHalf)
print(new.convert())
print(sub)

# Example 2: a set of integers
class intset(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        if e not in self.vals:
            self.vals.append(e)
        return self.vals
    def member(self,e):
        return e in self.vals
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

s = intset()
s.insert(5)
print(s.member(3))
print(s)
'''

########################################
# Why OOP
########################################
# 1.
class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age = newage
    def set_name(self,newname):
        self.name = newname
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)
# getter and setter could be used outside of class to access data attributes
myAnimal = Animal(3)
# print(myAnimal)
myAnimal.set_name('chang')
# print(myAnimal)

########################################
# Hierarchies:
########################################
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age) # override behaviour

jelly = Cat(1)
print(jelly.get_name())
jelly.set_name('JellyBelly')
print(jelly.get_name())
print(jelly)

class Rabbit(Animal):
    def speak(self):
        return "meep"
    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)

Peter = Rabbit(5)
print(jelly.speak())
print(Peter.speak())