def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Leitura do número de termos desejados
while True:
    try:
        n = int(input("Digite o número de termos da sequência de Fibonacci (n > 0): "))
        if n > 0:
            break
        else:
            print("Por favor, digite um número maior que 0.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Geração e exibição da sequência de Fibonacci
resultado = fibonacci(n)
print(f"Os primeiros {n} termos da sequência de Fibonacci são: {resultado}")
