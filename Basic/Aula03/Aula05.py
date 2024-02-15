b = 0
c = 0
for x in range(6):
    a = float(input(f"Digite o {x}º valor: "))
    if (a > 0):
        b = b + 1
        c = c + a


print(f"Valores positivos foram {b}")
print(f"A media foi {c/b:,.1f}")