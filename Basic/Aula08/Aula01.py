def sumTo(aBound):

    theSum = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum += aNumber
        aNumber += 1

    return theSum

print(sumTo(4))

eve_nums = []
n = 0
while n<=15:
    if n % 2==0:
        eve_nums.append(n)
    n +=1
list1 = [8, 3, 4, 5, 6, 7, 9]

accum = 0
x = 0
while x < len(list1):
    accum += list1[x]
    x += 1

print(accum)

def stop_at_four1():
    a = []
    while True:
        x = int(input("Digite:"))
        if x == 4:
            break
        a.append(x)
    return a


def stop_at_four(y):
    a = []
    t = 0
    while t < len(y):
        if y[t] == 4:
            break
        a.append(y[t])
        t +=1
    return a



print(stop_at_four([1,2,3,4]))