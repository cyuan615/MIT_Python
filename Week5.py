##############################
# define class
##############################
# class Classname(object): Chang's example
#     <define attributes here>
"""
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

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if name not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self,other):
        diff = self.get_age() - other.get_age()
        return diff
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

Eric = Person('eric',45)
print(Eric)
other = Person('Cindy',18)
print(Eric.age_diff(other))

import random

class Student(Person):
    def __init__(self,name,age,major = None):
        Person.__init__(self,name,age)
        self.major = major
    def change_major(self,major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print('i have homework')
        elif 0.25 < r <= 0.5:
            print('i need sleep')
        elif 0.5 < r <= 0.75:
            print('i should eat')
        else:
            print('i am watching TV')
    def __str__(self):
        return "student" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)

cindy = Student('Cindy',25,'cs')
print(cindy)
print(cindy.speak())
cindy.change_major('ba')
print(cindy)


########################################
# Class Variables:
########################################
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

class Rabbit(Animal):
    tag = 1
    def __init__(self,age,parent1 = None, parent2 = None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1 # tag used to give unique id to each new Rabbit instance
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other)
    def __eq__(self,other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_opposite or parents_same



peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1,peter,hopsy)
# print(cotton)
# print(cotton.get_parent1)


mopsy = peter + hopsy   # define + operator
mopsy.set_name('Mopsy')
# print(mopsy.get_parent1())
# print(mopsy.get_parent2())
print(cotton.rid)
print(mopsy.rid)
print(mopsy.__eq__(cotton))
"""

########################################
# Building a class
########################################
import datetime
class Person(object):
    def __init__(self,name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName

    def __str__(self):
        return self.name

    def setBirthday(self,month,day,year):
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self,other): # sort function
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

# cindy = Person('Cindy Yuan')
# cindy.setBirthday(6,15,1992)
# print(cindy.lastName)
# print(cindy.birthday)
# print(cindy.getAge())

# p1 = Person('Chang Liu')
# p1.setBirthday(5,7,1993)
# p2 = Person('Cindy Yuan')
# p2.setBirthday(6,15,1992)
# p3 = Person('Qian Lin')
# p3.setBirthday(8,14,1995)
#
# personList = [p1,p2,p3]
# personList.sort()
#
# for e in personList:
#     print(e)
#


class MITPerson(Person):

    nextIdNum = 0

    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self,other):
        return self.idNum < other.idNum

    def speak(self,utterance):
        return (self.getLastName() + "says: " + utterance)



