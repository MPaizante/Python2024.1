
n = int(input("Numero de funcionarios: "))
h = float(input("Horas trabalhadas: "))
s = float(input("Dinheiro por hora trabalhada: "))
def salary(n,h,s):
    return print("o numero de funcionario é:",n,"e o salario deles é:","{0:.2f}".format(h*s))
print(salary(n,h,s))