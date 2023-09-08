pr1 = float(input("\ndigite pr1: "))
pr2 = float(input("\ndigite pr2: "))
mf = (pr1 + pr2) / 2
print(f"\nmedia truncada = {int((mf - 0.5) + 0.001)}")
print(f"\nmedia arredondada = {int(mf + 0.001)}")
print("\n")