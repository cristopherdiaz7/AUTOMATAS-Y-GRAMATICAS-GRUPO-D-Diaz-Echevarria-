def reconocer_cadena(cadena):
    estado = 'inicio'

    for caracter in cadena:
        if estado == 'inicio':
            if caracter.isalpha():
                estado = 'entrada'
            else:
                return False  # No empieza con letra
        elif estado == 'entrada':
            if caracter.isalnum():
                estado = 'entrada'
            else:
                estado = 'final'
                break
        else:
            return False  # Estado inválido

    # Si terminó en un estado válido
    return estado == 'entrada'  # El final aceptado es cuando está aún en "entrada"

# Ejemplos de prueba
print(reconocer_cadena("abc123"))  # True
print(reconocer_cadena("123abc"))  # False
print(reconocer_cadena("abc$"))    # False
