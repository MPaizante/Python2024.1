class Point:
    def __init__(self,initX,initY) :
        self.x = initX
        self.y = initY
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distancia(self):
        res = ((self.x)**2+(self.y))**0.5
        return res
    def __str__(self):
        return f'Ponit: ({self.x},{self.y}) =  '
    
valores = input("Digite o ponto x e y: ").split()
valores_int = [int(n) for n in valores]
rs = Point(valores_int[0],valores_int[1])

print(rs)

class Cereal:
    def __init__(self,name,brand,fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber
        
    def __str__(self):
        return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!"

c1 = Cereal("Corn Flakes","Kellogg's",2)   
c2 = Cereal("Honey Nut Cheerios","General Mills",3 ) 
print(c1)