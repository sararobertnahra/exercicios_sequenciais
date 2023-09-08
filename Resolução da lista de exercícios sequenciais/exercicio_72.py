deposito = float(input("\nentre com depósito: "))
taxa = float(input("\nentre com taxa de juros: "))

valor = deposito * taxa / 100
total = deposito + valor

print(f"\nRendimentos: {valor} \nTotal: {total}")
print("\n")

