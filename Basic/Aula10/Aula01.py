a = ["Matheu","Paizante","de","Araujo"]
x = sorted(a)
print(x)
b = [3,4,2,7,9,6,8,1,5]

print(sorted(a, reverse= True))
print(sorted(b,reverse=False))
print(sorted(b,reverse=True))
b.sort()
print(b)

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse= True)

l1 =[1,7,4,-2,3]
print('-'*20 )
def ab(x):
    if x >=0:
        return x
    else:
        return  -x

l2 = sorted(l1,key=ab)
print(l2)
print(sorted(l1,reverse= True, key= ab))