class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(7,6)
print(p.getX())
print(p.getY())
print(p.distanceFromOrigin())
print('==================================================================')
class Animal():
    def __init__(self,arms,legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs
spider = Animal(4,4)
spidlimbs = spider.limbs()

