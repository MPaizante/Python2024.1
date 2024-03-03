def x (n):
    nw = filter(lambda a: a % 2 ==0 ,n)
    return list(nw)

print(x([3,4,6,7,0,1,9,5]))

def x2 (n):
    nw = filter(lambda a: a[-1] == 'a'  or a[0] == 'a',n)
    return list(nw)

print(x2(['carro','casa','sol','filho','roda','acender','abacaxi']))



lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
i = filter(lambda aw: 'w' in aw,lst_check)
filter_testing = list(i)
print(filter_testing)

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
o = filter(lambda o: 'o' in o,lst)
lst2 =list(o)
print(lst2)