listas_de_numero=[]
numero1=int(input("Introduce un número: "))
numero2=int(input("Introduce otro número: "))
numero3=int(input("Introduce otro número: "))
listas_de_numero.append(numero1)
listas_de_numero.append(numero2)
listas_de_numero.append(numero3)
print(listas_de_numero)
while listas_de_numero[0]==0:
  listas_de_numero[0]=int(input("Introduce un número distinto de 0: "))
if listas_de_numero[0]<listas_de_numero[1] and listas_de_numero[1]<listas_de_numero[2]:
      print("Los números están en orden de ascendente.")
else:
      print("Los números no están en orden de ascendente.")