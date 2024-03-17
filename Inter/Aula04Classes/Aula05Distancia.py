class Point:
    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

def distance(point1, point2):
    xdiff = point2.getX()-point1.getX()
    ydiff = point2.getY()-point1.getY()

    dist = (xdiff**2 + ydiff**2)**0.5

    return dist

p = Point(4,3)
q = Point(0,0)
print(distance(p,q))

a = Point(1,0)
b = Point(5,6)
def soma(a,b):
    s1 = a.getX() + b.getX()
    s2= a.getY() + b.getY()
    s= s1+s2
    return  s
print(soma(a,b))