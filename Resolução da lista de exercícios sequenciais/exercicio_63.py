na = float(input("\nhoras trabalhadas: "))
vha = float(input("\nvalor da hora-aula: "))
pd = float(input("\npercentual de desconto: "))

sb = na * vha
td = (pd / 100) * sb
sl = sb - td

print(f"\nsalario liquido: {sl}")
print("\n")