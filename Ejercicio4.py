usuario_edad = int(input("¿Cuántos años tiene? "))
ingresos = float(input("Escriba su ingreso mensual: "))

IMPUESTO = 1000

if usuario_edad >= 17 and ingresos >= IMPUESTO:
    print("Usted puede atributar")


else:
    print("Usted aún no puede atributar")
    