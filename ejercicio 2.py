def reconocer_cadena(cadena):
    estado = 'inicio'

    for caracter in cadena:
        if estado == 'inicio':
            if caracter.isalpha():
                estado = 'entrada'
            else:
                return False
        elif estado == 'entrada':
            if caracter.isalnum():
                estado = 'entrada'
            else:
                estado = 'final'
                break
        else:
            return False


    return estado == 'entrada'

# Ejemplos
print(reconocer_cadena("abc123"))
print(reconocer_cadena("123abc"))
print(reconocer_cadena("abc$"))
