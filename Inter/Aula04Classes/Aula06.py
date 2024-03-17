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

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7,6)
print(p)

print('===========================================================================')

class Cereal:
    def __init__(self, name,brand, fiber):
        self.n = name
        self.b = brand
        self.f = fiber

    def getN(self):
        return self.n
    def getB(self):
        return self.b
    def getF(self):
        return self.f
    def __str__(self):
        return f'{self.n} cereal is produced by {self.b} and has {self.f} grams of fiber in every serving!'

c1 = Cereal("Corn Flakes","Kellogg's",2)
c2 = Cereal("Honey Nut Cheerios","General Mills", 3)

print(c1)
print(c2)