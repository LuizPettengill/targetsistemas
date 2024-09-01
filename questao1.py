# Função que define a série de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a

# Função que checa se o numero digitado pertence a série de fibonacci
def belongs_fibonacci(number):
    if number < 0:
        return False
    
    fib_num = fibonacci(number)
    return fib_num == number

# Input do numero para o usuario
number = int(input("Escreva um número: "))

# Condicionais que chamam as funções para gerar o resultado final
if belongs_fibonacci(number):
    print(f"{number} é Fibonacci.")
else:
    print(f"{number} NÃO é Fibonacci.")
