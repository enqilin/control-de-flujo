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