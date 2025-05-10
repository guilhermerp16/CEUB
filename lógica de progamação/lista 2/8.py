n = int(input("Digite um número inteiro positivo: "))
a, b = 1, 1
print("Sequência de Fibonacci:")
print(a, end=" ")

for _ in range(n - 1):
    print(b, end=" ")
    a, b = b, a + b