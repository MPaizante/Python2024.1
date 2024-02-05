s = int(input("Informe os segundos: "))

minutos = s//60
horas = minutos//60
minutos= minutos % 60
s = s % 60

print(horas,":", minutos,":",s)