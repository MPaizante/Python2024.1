l1 = [1,2,3]
l2 = [4,5,6]
l3 = []
l4 = list(zip(l1,l2))
for i in range(len(l1)):
    l3.append(l1[i] + l2[i])

print(l3)
for u, i in l4:
    print(u+i)
print(l4)

print('-'*50)

l5=[a / b for a,b in list(zip(l1,l2))]
print(l5)

