entrada = int(input())
x = int(input())
y = int(input())
pares = []
sequencia = []
for i in range(entrada):
    if len(sequencia) == entrada:
        break
    sequencia.append(x)
    sequencia.append(y)
    x += y
    y += x
print(sequencia)

for i in sequencia:
    if i %2 == 0:
        pares.append(i)
print(pares)
quadrado = []
for i in sequencia:
    for u in range(i):
        if u**2 == i:

            quadrado.append(i)
print(quadrado)
