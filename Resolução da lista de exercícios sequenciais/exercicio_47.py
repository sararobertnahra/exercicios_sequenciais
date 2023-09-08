num = int(input("\nentre com um número de 3 dígitos: "))
c = num // 100
d = (num % 100) // 10
u = num % 10
num1 = u*100 + d*10 + c
print(f"\nnúmero: {num}")
print(f"\nnúmero invertido: {num1}")
print("\n")