frase = input("introduce una frase: ")
letra = input("introduce una letra: ")

# convertimos a todo en minúsculas ya que si alguien escribe la letra en mayúscula no detectará esa letra cuando sea minúscula y viceversa. 


contador = 0

for i in frase:
    if i == letra:
       
     contador += 1
print(f"letra '{letra}' se repite {contador} veces en esta frase '{frase}'.")



