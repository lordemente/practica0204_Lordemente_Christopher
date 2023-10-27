eco = ""

while True:
    repeat = input("Introduzca una palabra, o escriba 'salir' para finalizar: ")

    eco += repeat + "\n"

    if repeat.lower() == "salir":
        break

    print(eco)