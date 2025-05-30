transicion_afd = {
    0: {'a': 1, 'b': 2},
    1: {'a': 1, 'b': 2},
    2: {'a': 1, 'b': 2}
}

estado_inicial = 0
estados_finales = {1, 2}

def acepta_afd(cadena):
    estado = estado_inicial
    for simbolo in cadena:
        if simbolo in transicion_afd[estado]:
            estado = transicion_afd[estado][simbolo]
        else:
            return False
    return estado in estados_finales

print(acepta_afd("a"))
print(acepta_afd("bb"))
print(acepta_afd(""))
print(acepta_afd("abab"))
print(acepta_afd("c"))


