# Diccionario de compradores con nombre y función seleccionada
compradores = {}

# Stock inicial por función
stock_funciones = {
    "viernes": 150,
    "sabado": 180
}

# Función para comprar entrada
def comprar_entrada():
    if stock_funciones["viernes"] <= 0 and stock_funciones["sabado"] <= 0:
        print("No hay entradas disponibles para ninguna función.")
        return
    nombre = input("Ingrese su nombre: ").strip()
    if nombre in compradores:
        print("El nombre ya ha sido registrado.")
        return
    print("Seleccione función:")
    print("1. Cats Día Viernes")
    print("2. Cats Día Sábado")
    opcion = input("Ingrese opción (1 o 2): ").strip()

    if opcion == "1":
        if stock_funciones["viernes"] <= 0:
            print("Entradas agotadas para Cats Día Viernes.")
            return
        compradores[nombre] = "viernes"
        stock_funciones["viernes"] -= 1
        print("Entrada registrada exitosamente para Cats Día Viernes.")
    elif opcion == "2":
        if stock_funciones["sabado"] <= 0:
            print("Entradas agotadas para Cats Día Sábado.")
            return
        compradores[nombre] = "sabado"
        stock_funciones["sabado"] -= 1
        print("Entrada registrada exitosamente para Cats Día Sábado.")
    else:
        print("Opción de función inválida.")

# Función para cambio de función
def cambiar_funcion():
    nombre = input("Ingrese su nombre para buscar su entrada: ").strip()
    if nombre not in compradores:
        print("No se encontró una entrada con ese nombre.")
        return
    funcion_actual = compradores[nombre]
    nueva_funcion = "sabado" if funcion_actual == "viernes" else "viernes"

    print(f"Actualmente está en la función Cats Día {funcion_actual.capitalize()}.")
    confirmar = input(f"¿Desea cambiar a Cats Día {nueva_funcion.capitalize()}? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Cambio cancelado.")
        return

    if stock_funciones[nueva_funcion] <= 0:
        print("No hay stock disponible para la función seleccionada.")
        return

    # Realizar el cambio
    compradores[nombre] = nueva_funcion
    stock_funciones[funcion_actual] += 1
    stock_funciones[nueva_funcion] -= 1
    print(f"Cambio realizado a Cats Día {nueva_funcion.capitalize()}.")

# Función para mostrar el stock de funciones
def mostrar_stock():
    total_vendidos = len(compradores)
    print("Stock disponible:")
    print(f"Cats Día Viernes: {stock_funciones['viernes']} entradas disponibles")
    print(f"Cats Día Sábado : {stock_funciones['sabado']} entradas disponibles")
    print(f"Total entradas vendidas: {total_vendidos}")

# Función principal (main)
def main():
    while True:
        print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
        print("1.- Comprar entrada a Cats.")
        print("2.- Cambio de función.")
        print("3.- Mostrar stock de funciones.")
        print("4.- Salir.")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            cambiar_funcion()
        elif opcion == "3":
            mostrar_stock()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    main()
