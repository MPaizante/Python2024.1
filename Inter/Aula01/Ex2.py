L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]
test1 = ''
if 'hola' in L:
    test1 = 'True'
else:
    test1 = False
if [5, 8, 7] in L:
    test2 =True
else:
    test2 = False
if 6.6 in L:
    test3 = True
else:
    test3 = False


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}
data = 'data' in nested.keys()
twentyfour = 24 in nested.values()
print(twentyfour)
whole = 'whole' not in nested['window']
print(whole)
physics = ''
if 'physics' in nested:
    physics = True
else:
    physics = False


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d['London']['Great Britain']
print(london_gold)


sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}
v1 = sports['swimming'][2]
v2 = sports['diving'][1]
v3 = sports['gymnastics']['women']
v4 = sports['gymnastics']['men'][3]


