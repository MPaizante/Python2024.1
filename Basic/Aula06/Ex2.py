olympics = {'gold':7, 'silver':8,'bronze':6}
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012,"Brazil":2016}
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers ['Phelps'] = 28
a = []
for i in swimmers.keys():
    a.append(f'{i} possui {swimmers[i]} medalhas.')
a.sort()
for x in a:
    print(x)

b = list(swimmers.keys())
b.sort()
print(b)

print(list(swimmers.values()))
print(list(swimmers.items()))
inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())       # Make a list of all of the keys
print(ks)
print(ks[0])                      # Display the first key
