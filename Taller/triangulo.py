tamano = int(input("Digite el tamaño de la matriz: "))

matriz = []

for f in range(tamano):
    fila = []

    for c in range(tamano):
        if c <= f:
            if c % 2 == 0:
                fila.append("A")
            else:
                fila.append("B")
        else:
            fila.append("")

    matriz.append(fila)

for fila in matriz:
    for valor in fila:
        print(valor, end="\t")
    print()