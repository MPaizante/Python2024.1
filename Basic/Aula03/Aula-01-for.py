names = ["Matheus","Paizante","Araujo"]

for name in names:
    print("Olá",name,"você está bem?")


x = len(names)-1
print(x)

def fibonacci(n):
    fib_sequence = [0, 1]

    for x in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

# Exemplo: gerar os primeiros 10 números da sequência de Fibonacci
n = 30
fibonacci_sequence = fibonacci(n)
print(f"Fibonacci Sequence ({n} numbers): {fibonacci_sequence}")
