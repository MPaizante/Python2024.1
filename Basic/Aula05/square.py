import math;

file = open("square.txt","w")
for num in range(13):
    s = num*num
    file.write(f'{str(s)}'+ '\n')
file.close

x = open("square.txt" , "r")
print(x.read()[:10])
