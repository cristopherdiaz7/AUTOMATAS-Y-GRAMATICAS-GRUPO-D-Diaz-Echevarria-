estado_inicial = 'A'
estados_finales = {'A', 'B'}

transiciones = {
    'A': {'a': 'B', 'b': 'B'},
    'B': {'a': 'B', 'b': 'B'}
}

def procesar_cadena(cadena):
    estado_actual = estado_inicial

    for simbolo in cadena:
        if simbolo in transiciones[estado_actual]:
            estado_actual = transiciones[estado_actual][simbolo]
        else:
            return False

    return estado_actual in estados_finales

cadenas = ["", "a", "b", "ab", "ba", "abba", "bab", "bbb", "aaab", "aaaabb", "abab", "baba", "baabba", "bbbaaa"]
for cadena in cadenas:
    resultado = procesar_cadena(cadena)
    print(f"Cadena '{cadena}': {'ACCEPTADA' if resultado else 'RECHAZADA'}")
