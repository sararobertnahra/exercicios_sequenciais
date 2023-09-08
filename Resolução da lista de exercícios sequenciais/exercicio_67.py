valor = float(input("\ndigite o valor da prestação: "))
taxa = float(input("\ndigite a taxa: "))
tempo = int(input("\ndigite o tempo(numero de meses): "))

prest = valor + (valor*(taxa/100)*tempo)

print(f"\no valor da prestacao em atraso e = {prest}")
print("\n")

