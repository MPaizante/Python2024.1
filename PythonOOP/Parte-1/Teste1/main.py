import classes_parteUm
escritor = classes_parteUm.Escritor("João")
print(escritor.nome)
caneta = classes_parteUm.Caneta('Compactor')
maquina = classes_parteUm.MaquinaDeEscrever('Dell')
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()