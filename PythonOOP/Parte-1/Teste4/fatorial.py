def fatorial(n):
    if n == 1:
        return 1
    else:
        return n*(fatorial(n-1))
fat =fatorial(5)
print(fat)