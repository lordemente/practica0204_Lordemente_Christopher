núm = int(input("Introduce un número: "))

if núm <= 0:
    print("ingrese un numero superior a cero")

else:
    for fila in range(1, núm + 1):
        numero = 2 * fila - 1
        
        
        for i in range(fila):
            print(numero, end =" ")
            numero -= 2
            
        print()