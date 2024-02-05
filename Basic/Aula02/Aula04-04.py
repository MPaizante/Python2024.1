nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salario: "))
vendas = float(input("digite valor das vendas: "))

def s(nom,sal,ven):
    novo = float(sal) + float(ven)*0.15
    return print("O funcionario",nom,"vendeu",ven,"então sua seu salario será de ", round(novo,2))

print(s(nome,salario,vendas))