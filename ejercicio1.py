numero1=float(input("Introduce un número: "))
numero2=float(input("Introduce otro número: "))
numero3=float(input("Introduce otro número: "))

while numero1==0:
  numero1=float(input("Indrotuce un número distinto de 0"))
if numero1<numero2 and numero2<numero3:
  print("Los números están en orden de ascendente.")
else:
  print("Los números no están en orden de ascendente.")