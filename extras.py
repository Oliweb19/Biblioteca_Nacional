def menu():
    op = 0
    while (op != 6):
        print("--- Biblioteca Nacional ---")
        print("1. Agregar Libros")
        print("2. Eliminar Libros")
        print("3. Buscar Libros")
        print("4. Ver Libros")
        print("5. Buscar Libros por año")
        print("6. Salir")
        op = int(input("Ingrese un numero de las opciones: "))
        if (op < 0 or op > 6):
            print("La opcion no es valida")
        else:
            return op