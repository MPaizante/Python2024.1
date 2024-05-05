#entrada = str(input())
arquivo = open('test.txt','r')
texto = arquivo.readlines()
linha = 0
linhas =''
maior = ''
for i in texto:
    linha += 1
    for u in i.split():
        if len(maior) < len(u):
            linhas += str(linha) + ' '
            maior = u

print(f'A maior palavra é "{maior}" e se encontra na(s) linha(s): {linhas}')






arquivo.close()