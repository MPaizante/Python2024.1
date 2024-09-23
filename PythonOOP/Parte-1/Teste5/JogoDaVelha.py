import os
import random
from colorama import Fore,Back,Style

jogarNovamente = 's'
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = 'n'
velha = [[" " for i in range(3)] for j in range(3)]

def tela():
    global velha
    os.system('cls')
    print('    0     1      2')
    print('0:  ',velha[0][0],' | ',velha[0][1],' | ',velha[0][2])
    print('   ----------------')
    print('1:  ',velha[1][0],' | ',velha[1][1],' | ',velha[1][2])
    print('   ----------------')
    print('2:  ',velha[2][0],' | ',velha[2][1],' | ',velha[2][2])
    print(f'Jogadas: {Fore.GREEN } { jogadas} {Fore.RESET}')


def jogadorJoga():
    global  jogadas
    global  quemJoga
    global  vit
    global maxJogadas

    if quemJoga == 2 and jogadas<maxJogadas:
        try:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            while velha[linha][coluna] != " ":
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
            velha[linha][coluna] = "X"
            jogadas += 1
            quemJoga = 1
        except:
            print('Invalido!!!')

def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 1 and jogadas<maxJogadas:
        try:
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
            while velha[linha][coluna] != " ":
                linha = random.randrange(0, 3)
                coluna = random.randrange(0, 3)
            velha[linha][coluna] = "0"
            jogadas += 1
            quemJoga = 2
        except :
            print('Invalido!!!')

while True:
    tela()
    jogadorJoga()
    cpuJoga()