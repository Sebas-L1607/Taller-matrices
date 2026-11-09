def leer_producto():
    nombre = input("Digite el nombre del producto: ").strip()

    while nombre == "":
        nombre = input("El nombre no puede estar vacío. Digítelo nuevamente: ").strip()

    return nombre


def nombre_para_ordenar(producto):
    return producto[0].lower()


inventario = []
orden_ingreso = 0

while True:
    print("""
1. Agregar producto
2. Agregar lote de productos
3. Eliminar producto del inventario
4. Eliminar el producto más reciente
5. Ordenar productos alfabéticamente
6. Mostrar número total de productos
7. Salir
""")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        nombre = leer_producto()
        orden_ingreso += 1
        inventario.append((nombre, orden_ingreso))
        print(f"Producto agregado: {nombre}")

    elif opcion == "2":
        cantidad = int(input("¿Cuántos productos tiene el lote?: "))

        while cantidad <= 0:
            cantidad = int(input("Digite una cantidad mayor que cero: "))

        for numero in range(1, cantidad + 1):
            print(f"Producto {numero} del lote")
            nombre = leer_producto()
            orden_ingreso += 1
            inventario.append((nombre, orden_ingreso))

        print(f"Se agregaron {cantidad} productos.")

    elif opcion == "3":
        nombre = leer_producto()
        posicion_encontrada = -1

        for posicion in range(len(inventario)):
            if inventario[posicion][0].lower() == nombre.lower():
                posicion_encontrada = posicion
                break

        if posicion_encontrada == -1:
            print("El producto no está en el inventario.")
        else:
            eliminado = inventario.pop(posicion_encontrada)
            print(f"Producto eliminado: {eliminado[0]}")

    elif opcion == "4":
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            posicion_reciente = 0

            for posicion in range(1, len(inventario)):
                if inventario[posicion][1] > inventario[posicion_reciente][1]:
                    posicion_reciente = posicion

            eliminado = inventario.pop(posicion_reciente)
            print(f"Producto más reciente eliminado: {eliminado[0]}")

    elif opcion == "5":
        inventario.sort(key=nombre_para_ordenar)

        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            for producto in inventario:
                print(producto[0])

    elif opcion == "6":
        print(f"Total de productos: {len(inventario)}")

    elif opcion == "7":
        print("Programa terminado.")
        break

    else:
        print("Opción inválida.")