edad = int(input("Introduzca su edad: "))



if edad > 0:
    for i in range(1, edad + 1, +1):
        print(i, "años")

else:
    print("no se puede escribir 0 o años negativos, introduzca su edad de nuevo")
           
