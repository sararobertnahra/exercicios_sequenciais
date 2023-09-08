import math as m

angulo = float(input("\ndigite um angulo em graus: "))
rang = angulo*m.pi /180

print(f"\nseno: {m.sin(rang)}")
print(f"\nco-seno: {m.cos(rang)}")
print(f"\ntangente: {m.tan(rang)}")
print(f"\nco-secante: {1/m.sin(rang)}")
print(f"\nsecante: {1/m.cos(rang)}")
print(f"\ncotangente: {1/m.tan(rang)}")
print("\n")
