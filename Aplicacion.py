import sqlite3

# Conexión a la base de datos o creación si no existe
conn = sqlite3.connect('Apellidos_almacen.db')

# Creación de la tabla "Producto" si no existe
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Producto (
        idproducto INTEGER PRIMARY KEY,
        codigo TEXT,
        nombre TEXT,
        precio REAL
    )
''')

# Lista para almacenar elementos
elementos = []

while True:
    # Mostrar el menú de opciones
    print("Menú Opciones")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a registrar: ")
        elementos.append(elemento)
        print("Elemento registrado con éxito.")
    elif opcion == "2":
        if elementos:
            print("Elementos disponibles:")
            for i, elemento in enumerate(elementos):
                print(f"{i+1}. {elemento}")
            indice = int(input("Ingrese el número del elemento a eliminar: ")) - 1
            if 0 <= indice < len(elementos):
                elementos.pop(indice)
                print("Elemento eliminado con éxito.")
            else:
                print("Índice no válido.")
        else:
            print("No hay elementos para eliminar.")
    elif opcion == "3":
        if elementos:
            print("Elementos disponibles:")
            for i, elemento in enumerate(elementos):
                print(f"{i+1}. {elemento}")
            indice = int(input("Ingrese el número del elemento a editar: ")) - 1
            if 0 <= indice < len(elementos):
                nuevo_elemento = input("Ingrese el nuevo valor del elemento: ")
                elementos[indice] = nuevo_elemento
                print("Elemento editado con éxito.")
            else:
                print("Índice no válido.")
        else:
            print("No hay elementos para editar.")
    elif opcion == "4":
        if elementos:
            print("Elementos disponibles:")
            for i, elemento in enumerate(elementos):
                print(f"{i+1}. {elemento}")
        else:
            print("No hay elementos para mostrar.")
    elif opcion == "5":
        # Salir del programa y cerrar la conexión a la base de datos
        print("Saliendo del programa. ¡Hasta luego!")
        conn.close()
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")

