numeros=[1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
  numero*=10
  print(numero, end=",")


listas_de_palabras=['manzana','atletista','bandminton','submarino']
for palabras in listas_de_palabras:
  print(palabras,len(palabras))



contador=0

while True :
  frases=str(input("Escribir frases: "))
  lower_frases=frases.lower()
  for punto in lower_frases:
    if punto == "a":
      contador+=1
  if punto==".":
    break
print("La 'a' ha aparecido ",contador, "veces")
listas_de_palabras=['manzana','atletista','bandminton','submarino']
for palabras in listas_de_palabras:
  print(palabras,len(palabras))
print(len(palabras))

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
      