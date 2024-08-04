class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
point1 = Point(7,6)
print(f'Os pontos são ({point1.getX()},{point1.getY()}) a distancia da origem é {point1.distanceFromOrigin():,.1f}')



class Animal(object):
    def __init__(self, arms,legs):
        self.arms = arms
        self.legs = legs
    def limbs(self):
        return self.arms + self.legs

spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)
        
    
