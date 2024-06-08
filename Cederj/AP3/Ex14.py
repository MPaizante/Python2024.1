entrada = input('Digite: ')
d = {}
with open(entrada,'r') as arquivo:
    for i in arquivo:
        linha  = i.split()
        for j in linha:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
print(d)
maiores = []
for i in d:
    if d[i] > 5:
        maiores.append(i)

for i in range(len(maiores)):
    for j in range(1,len(maiores)-i):
        if maiores[j-1]>maiores[j]:
            maiores[j-1],maiores[j] = maiores[j], maiores[j-1]
for i in maiores:
    print(i)
