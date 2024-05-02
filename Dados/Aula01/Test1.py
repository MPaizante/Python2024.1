l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for i in l_of_l:
    third.append(i[2])

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []
for i in athletes:
    for u in i:
        if 't' in u or 'T' in u:
            t.append(u)
        else:
            other.append(u)

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
yellow = ''
four = 0
orange = ''
for i in lst:
    for u in i:
        if u == 'yellow':
            yellow = True
        if u == 4:
            four = u
        if u == 'orange':
            orange = True

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]
test1 = ('hola' in L)
test2 = ([5, 8, 7] in L)
test3 = (6.6 in L[2])


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}
data = True
twentyfour = (24 in nested.keys())
whole = ('whole ' in nested.keys())
physics = ('physics' in nested.keys())




nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = 0
for i,t in nested_d.items():
    print(i , t)
    if i == 'London':
        for u,k in t.items():
            if u == 'Great Britain':
                london_gold += k

print(london_gold)

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

for i in sports['swimming']:
    if i == 'backstroke':
        v1 = i
if 'platform' in sports:
    v2 = 'platform'

v3 = ['vault', 'floor', 'uneven bars', 'balance beam']
if 'rings' in sports:
    v4 = 'rings'
print("-"*50)
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
US_count = []
for i, j in nested_d.items():
    for u,t in j.items():
        if u == "USA":
            US_count.append(t)
print(US_count)


