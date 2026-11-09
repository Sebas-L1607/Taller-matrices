def superReducedString(s):
    letras = []

    for letra in s:
        if len(letras) > 0 and letras[-1] == letra:
            letras.pop()
        else:
            letras.append(letra)

    if len(letras) == 0:
        return "Empty String"

    return "".join(letras)


texto = input("Digite la cadena: ")
print(superReducedString(texto))