idade_em_dias = int(input("Digite a idade em dias: "))

# Calcula anos, meses e dias
anos = idade_em_dias // 365
idade_em_dias %= 365

meses = idade_em_dias // 30
idade_em_dias %= 30

dias = idade_em_dias

# Exibe o resultado
print(f"{anos} anos, {meses} meses e {dias} dias.")