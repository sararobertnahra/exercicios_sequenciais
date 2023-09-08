p = float(input("\ndigite o valor da aplicacao: "))
i = float(input("\ndigite a taxa (0 - 1): "))
n = int(input("\ndigite o numero de meses: "))

va = p * (((1 + i ) ** n) - 1) / i

print(f"\nO valor acumulado {va}")
print("\n")
