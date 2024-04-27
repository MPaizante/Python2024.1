x = {}
x['um'] = 1
x['dois'] = 2
x['tres'] = 3
x['quatro'] = 4
x['cinco'] = 5
print(x)
print('='*100)
val = x['um']
print(val,'-----------' ,x['um'])
medals = { 'silver': 8,'gold':7, 'bronze': 6}
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012, 'Brazil':2016}
print(places)
del places['Brazil']
print(places)
places.pop('China')
print(len(places))
x['um'] = x['um'] + 5
print(x)
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}

swimmers['Phelps'] = swimmers['Phelps'] + 5
for i in swimmers:
    print(f'Total de medalhas de {i}, são {swimmers[i]}')
print(swimmers.keys())
print(swimmers.values())
print(list(swimmers.items()))

