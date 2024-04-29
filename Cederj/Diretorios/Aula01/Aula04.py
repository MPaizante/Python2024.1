travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0
for i in travel.values():
    total += i
print(total)

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits = 0
for i in schedule.values():
    total_credits += i


d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = 0
for k in d:
    if d[k]> ks:
        ks = d[k]


print(ks)
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for i in placement:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] +1

print(d)
x = d['a']
min_value = ''
for i in d:
    if d[i] < x:
        min_value =  i
print(min_value)


product = "iphone and android phones"
lett_d = {}
for i in product:
    if i not in lett_d:
        lett_d[i] = 1
    else:
        lett_d[i] += 1

max_value = ''
x = 0
for i in lett_d:
    if lett_d[i] > x:
        x = lett_d[i]
        max_value = i
print(max_value, '====',x)
