entrada_str = input().split()
entrada_numeros = [int(num) for num in entrada_str]


def maior(x):
    m = x[0]
    for i in x:
        if i >m:
            m = i
    return m
def menor(x):
    m = x[0]
    for i in x:
        if m < i :
            m = i
    return m
def media(x):
    c = 0
    soma = 0
    for i in x:
        if i % 2 ==0:
            soma += i
            c +=1
    res = soma/c
    return res


print(f"O maior é {maior(entrada_numeros)}")
print(f"O menor é {menor(entrada_numeros)}")
print(f"A media dos pares é {media(entrada_numeros):,.1f}")


