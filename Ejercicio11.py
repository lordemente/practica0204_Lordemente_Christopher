palabra = input("Introduzca una palabra: ")

for i in palabra[::-1]:  #importante debe estar entre corchetes.
    print(i)


"""""
 Este codigo invierte orden del string de manera horizontal
palabra = input("Introduce una palabra: ")

# Mostrar las letras en orden inverso de manera horizontal
print("La palabra en orden inverso es:", end="")
for letra in palabra[::-1]:
    print(letra, end="")
print()  # Para imprimir un salto de línea al final
"""