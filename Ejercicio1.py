variable = "contraseña"

contraseña = input("Introduce la contraseña: ")

if contraseña.lower() == variable.lower():
    print("Contraseña correcta, pase joven")
else:
    print("Contraseña incorrecta, intentelo de nuevo")