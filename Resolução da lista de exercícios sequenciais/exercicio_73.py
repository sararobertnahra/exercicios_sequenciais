num = float(input("\nentre com um numero com parte fracionaria: "))
numi = int(num - 0.5)
numfrac = num - numi
numa = int(num + 0.00001)

print(f"\nparte inteira: {numi}")
print(f"\nparte fracionaria: {(numfrac + 0.00001):.3f}")
print(f"\nnumero arredondado: {numa}")
print("\n")