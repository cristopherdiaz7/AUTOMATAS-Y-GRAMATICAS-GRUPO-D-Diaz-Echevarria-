estado_inicial = 0
estados_finales = {1}

transiciones = {
    0: {'a': [0, 1], 'b': [0, 1], 'ε': [1]},
    1: {}
}


def mover(estado_actual, simbolo):

    if simbolo in transiciones[estado_actual]:
        return transiciones[estado_actual][simbolo]
    else:
        return []


def epsilon_clausura(estados):

    pila = list(estados)
    cerradura = set(estados)

    while pila:
        estado = pila.pop()
        if 'ε' in transiciones[estado]:
            for destino in transiciones[estado]['ε']:
                if destino not in cerradura:
                    cerradura.add(destino)
                    pila.append(destino)
    return cerradura


def procesar_cadena(cadena):

    estados_actuales = epsilon_clausura({estado_inicial})

    for simbolo in cadena:
        nuevos_estados = set()
        for estado in estados_actuales:
            posibles_destinos = mover(estado, simbolo)
            for destino in posibles_destinos:
                nuevos_estados.update(epsilon_clausura({destino}))
        estados_actuales = nuevos_estados

    return any(estado in estados_finales for estado in estados_actuales)


cadenas = ["", "a", "b", "ab", "ba", "abba", "bab", "bbb", "aaab", "aaaabb", "abab", "baba", "baabba""bbbbb bb"]
for cadena in cadenas:
    resultado = procesar_cadena(cadena)
    print(f"Cadena '{cadena}': {'ACCEPTADA' if resultado else 'RECHAZADA'}")
