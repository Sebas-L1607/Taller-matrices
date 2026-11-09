tamano = int(input("Digite el tamaño de la matriz: "))

matriz = []
numero = 1

for f in range(tamano):
    fila = []

    for c in range(tamano):
        fila.append(numero)
        numero += 1

    matriz.append(fila)

for fila in matriz:
    for valor in fila:
        print(valor, end="\t")
    print()