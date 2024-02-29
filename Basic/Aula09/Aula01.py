def f(x = 0, y = 1):
    return x * y

print(f())

def str_mult(x, y = 3):
    res = x * y
    return res


names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))



def multiply(x,mult_int = 10):
    return x * mult_int

print(multiply('Hello',mult_int=3))



def waste( mar,var = "Water", marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string

print(type(waste))
l= lambda x :x -1
print(l(10))

last =  lambda  s: s[-1]
print(last([1,2]))
