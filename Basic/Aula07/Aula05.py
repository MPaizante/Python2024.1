def addit(x):
    return x+5


def mult(y):
    return addit(y)* y

print(mult(5))



def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)