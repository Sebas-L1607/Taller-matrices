tamano = int(input("Digite el tamaño de la matriz: "))

matriz = []

for f in range(tamano):
    fila = []

    for c in range(tamano):
        if f % 2 == 0:
            fila.append(c + 1)
        else:
            fila.append(tamano - c)

    matriz.append(fila)

for fila in matriz:
    for valor in fila:
        print(valor, end="\t")
    print()