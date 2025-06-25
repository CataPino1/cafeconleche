def sumar_tres_valores():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        resultado = num1 + num2 + num3
        print(f"La suma de los tres valores es: {resultado}")
    except ValueError:
        print("Debe ingresar solo números válidos.")

# Llamada a la función principal
sumar_tres_valores()
