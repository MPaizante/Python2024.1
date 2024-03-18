class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point ({self.x},{self.y})'
    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

p1 = Point(-5,10)
p2 = Point( 15,20)
print(p1)
print(p2)
print(p1 + p2 )
print(p1 - p2)

print('='*60)

class Fruit:
    def __init__(self, name, price):
        self.n = name
        self.p = price
    def sorty(self):
        return self.p
l = [
    Fruit('Cherry', 18),
    Fruit('Apple', 5),
    Fruit('Bluebbery', 20)
]
print(sorted(l, key=Fruit.sorty))

for f in sorted(l,key=Fruit.sorty):
    print(f.n, f.p)
print('----------------------------------------')
for f in sorted(l, key=lambda x: x.sorty()):
    print(f.n)