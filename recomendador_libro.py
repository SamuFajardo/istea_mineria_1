class Libro:
   def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor=autor
        self.genero = genero
        self.puntuacion= puntuacion
        
        
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)

lista_libros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]

while True:
    print("\n¿Qué acción quieres realizar?")
    print("1. Agregar Libro")
    print("2. Buscar Libros por Género")
    print("3. Recomendar Libro")
    print("4. Salir")
    
    opcion = input("Ingresa el número de la acción: ")
    
    if opcion == "1":
        titulo = input("Ingresa el título del libro: ")
        autor = input("Ingresa el autor del libro: ")
        genero = input("Ingresa el género del libro: ")
        puntuacion = float(input("Ingresa la puntuación del libro: "))
        
        nuevo_libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(nuevo_libro)
        print("Libro agregado exitosamente.")
        
    elif opcion == "2":
        genero_busqueda = input("Ingresa el género que deseas buscar: ")
        libros_en_genero = [libro.titulo for libro in lista_libros if libro.genero == genero_busqueda]
        if libros_en_genero:
            print(f"Libros en el género '{genero_busqueda}':")
            for titulo in libros_en_genero:
                print("- " + titulo)
        else:
            print(f"No se encontraron libros en el género '{genero_busqueda}'.")
        
    elif opcion == "3":
        genero_recomendacion = input("Ingresa tu género de interés: ")
        libros_en_genero = [libro for libro in lista_libros if libro.genero == genero_recomendacion]
        if libros_en_genero:
            libro_recomendado = max(libros_en_genero, key=lambda libro: libro.puntuacion)
            print(f"Recomendación: {libro_recomendado.titulo} (Puntuación: {libro_recomendado.puntuacion})")
        else:
            print(f"No se encontraron libros en el género '{genero_recomendacion}' para recomendar.")
        
    elif opcion == "4":
        print("Saliendo del programa.")
        break
        
    else:
        print("Opción inválida. Por favor, ingresa un número válido.")



