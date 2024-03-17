cityNames= ['Detroid', 'Ann Anrbor', 'Pittsburgh', 'Mars', 'New York']
population = [ 680250, 117070 , 304391, 183, 84006000]
states = ['MI', 'WI', 'PA', 'PA' , 'NY']
citytuples = zip(cityNames,population,states)
class City:
    def __init__(self, n , p , s):
        self.name = n
        self.population = p
        self.state = s
    def __str__(self):
        return f'{self.name}, {self.population} (pop:{self.state})'

cities =[]
for c in citytuples:
    name, pop, state = c
    citys = City(name, pop, state)
    print(citys)
    cities.append(citys)

print(cities)