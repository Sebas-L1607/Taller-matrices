def solution(a):
    peso_equipo_1 = 0
    peso_equipo_2 = 0

    for posicion in range(len(a)):
        if posicion % 2 == 0:
            peso_equipo_1 += a[posicion]
        else:
            peso_equipo_2 += a[posicion]

    return [peso_equipo_1, peso_equipo_2]