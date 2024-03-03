lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = list(map(lambda x: 'Fruit: '+ x,lst_check))
print(map_testing)

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = list(filter(lambda x: x[0] == 'B',countries))
print(b_countries)








people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [p[1] for p in people]
print(first_names)

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [n * 2 for n in lst]
print(lst2)

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [w[0] for w in students if w[1]>=70]
print(passed)


l1 = ['left', 'up', 'front']
l2 = ['right', 'back', 'down']
x = tuple(filter(lambda x: len(x)>3,l1))
y = tuple(filter(lambda x: len(x)>3,l2))
print((y))
print((x))
opposites = [(a , b)  for a,b in zip(x,y)]
print(opposites)


species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = [(x,c) for x,c in zip(species,population)]
print(pop_info)
endangered = [m for m,n in pop_info if n <2500]
print(endangered)

