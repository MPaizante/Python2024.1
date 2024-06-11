dicionarioPessoas = dict()
nome = input()
while nome != "":
    sexo, idade, altura, peso = input().split()
    idade, altura, peso = int(idade), float(altura), float(peso)
    dicionarioPessoas[nome] = sexo, idade, altura, peso
    nome = input()
def mostra(dPs):
    if len(dPs) == 0:
        print("Nenhuma pessoa foi inserida no dicionário!")
    else:
        print("Dicionário de Pessoas Inseridas:")
        for nome, dados in sorted(dPs.items()):
            sexo, idade, altura, peso = dados
            print(nome, sexo, idade, altura, peso)

mostra(dicionarioPessoas)