class Point():
    def getX(self):
        return self.x


Point1 = Point()
Point2 = Point()
Point1.x = 10
Point2.x = 20
print(Point1.getX())
print(Point2.getX())