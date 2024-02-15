x = int(input("Quantos numeros você quer ler ?:"))
b = 0
c = 0
for y in range(x):
    d = int(input("Digite o numero:"))
    if 10<=d<=20:
        b += 1
    else:
        c += 1

print(f"{b} in")
print(f"{c} out")