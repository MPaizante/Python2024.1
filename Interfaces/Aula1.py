class Point2():
    def getX(self):
        return self.x
        

point1 = Point2()
point2 = Point2()
point1.x = "A"
print(point1.getX())

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):

        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print("Nothing seems to have happened with the points","(",p.x,",",p.y,")")


class NumberSet ():
    def getnum1(self):
        return self.num1
    def getnum2(self):
        return self.num2

t = NumberSet()
t.num1 = 6
t.num2 = 10

print("---------------------")

class NumberSet ():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return print(num1,num2)
t = NumberSet(6,10)

