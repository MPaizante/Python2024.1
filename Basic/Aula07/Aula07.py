practice = ('y','h','z','x')

tup1 = ('a','b','c')

lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = []
for i in lst_tups:
    t_check.append(i[2])

print(t_check)

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds = []
for i in tups:
    seconds.append(i[1])

def information(name,birth_year,fav_color,hometown):
    return  (name,birth_year,fav_color,hometown)

def info(name,age,birth_year,year_in_college,hometown):
    return (name,age,birth_year,year_in_college,hometown)

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

water, fire, electirc,grass = "Squirtle","Charmander","Pikachu","Bulbasaur"

v1, v2, v3,v4 =1, 2, 3, 4

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for i,k in pokemon.items():
    p_names.append(i)
    p_number.append(k)

print(p_number)
print(p_names)


track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events= []
for i in track_medal_counts.items():
    track_events.append(i)

