tamano = int(input("Digite el tamaño de la matriz: "))

matriz = []

for f in range(tamano):
    fila = []

    for c in range(tamano):
        if c <= f:
            fila.append(1)
        else:
            fila.append(0)

    matriz.append(fila)

for fila in matriz:
    for valor in fila:
        print(valor, end="\t")
    print()