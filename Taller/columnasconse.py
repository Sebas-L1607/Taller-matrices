tamano = int(input("Digite el tamaño de la matriz: "))

matriz = []

for f in range(tamano):
    fila = []

    for c in range(tamano):
        numero = c * tamano + f + 1
        fila.append(numero)

    matriz.append(fila)

for fila in matriz:
    for valor in fila:
        print(valor, end="\t")
    print()