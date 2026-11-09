def lsttotalesprodxsem(ventas, precios):
    filas = len(ventas)
    columnas = len(ventas[0])
    lsttotales = []

    for f in range(filas):
        suma = 0

        for c in range(columnas):
            suma += ventas[f][c] * precios[f]

        lsttotales.append(suma)

    return lsttotales


def mayordiaventas(ventas, precios):
    filas = len(ventas)
    columnas = len(ventas[0])
    mayorventa = []

    for k in range(columnas):
        sumas = 0

        for l in range(filas):
            sumas += ventas[l][k] * precios[l]

        mayorventa.append(sumas)

    return mayorventa


dias = ["lunes", "martes", "miércoles", "jueves",
        "viernes", "sábado", "domingo"]

matventas = []
lstprecios = []

# Pedir el precio y las ventas de cada producto.
for producto in range(1, 6):
    print(f"\nProducto {producto}")

    precio = int(input("Digite el precio unitario en pesos: "))

    while precio <= 0:
        precio = int(input("El precio debe ser mayor que cero. Digítelo nuevamente: "))

    lstprecios.append(precio)
    fila_ventas = []

    for dia in dias:
        unidades = int(input(f"Digite las unidades vendidas el {dia}: "))

        while unidades < 0:
            unidades = int(input(f"Las unidades del {dia} no pueden ser negativas. Digítelas nuevamente: "))

        fila_ventas.append(unidades)

    matventas.append(fila_ventas)


# Calcular los ingresos de cada producto y cada día.
lsttotales = lsttotalesprodxsem(matventas, lstprecios)
mayorventa = mayordiaventas(matventas, lstprecios)

maxtotal = max(lsttotales)
prodventmax = lsttotales.index(maxtotal) + 1

maxdiaventas = max(mayorventa)
posicion_dia = mayorventa.index(maxdiaventas)
dia_mayor_venta = dias[posicion_dia]

print(f"\nEl producto con mayores ingresos fue el {prodventmax}, con ${maxtotal:,}.")
print(f"El día con mayores ingresos fue el {dia_mayor_venta}, con ${maxdiaventas:,}.")