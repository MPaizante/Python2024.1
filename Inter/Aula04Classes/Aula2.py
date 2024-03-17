class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x


Point1 = Point(5,10)
Point2 = Point(1,2)
print(Point1.getX())

class P():
    def __init__(self,x , y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

po = P(10,100)
print(po.x)