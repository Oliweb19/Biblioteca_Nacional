def agg_libro():
    print("--- Agregar Libro ---")
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    ano = input("Ingrese el año de publicacion del libro: ")
    genero = input("Ingrese el genero del libro: ")

    libros = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "genero": genero
    }
    return libros