AFN = {
    0: {'a': [0], 'b': [0], 'ε': [1]},
    1: {'a': [2], 'b': [2], 'ε': [2]},
    2: {}
}

estados_finales = {2}
estado_inicial = 0

def epsilon_closure(estados):
    stack = list(estados)
    closure = set(estados)
    while stack:
        estado = stack.pop()
        for destino in AFN.get(estado, {}).get('ε', []):
            if destino not in closure:
                closure.add(destino)
                stack.append(destino)
    return closure

def mover(estados, simbolo):
    resultado = set()
    for estado in estados:
        resultado.update(AFN.get(estado, {}).get(simbolo, []))
    return resultado

def acepta_afn(cadena):
    actuales = epsilon_closure({estado_inicial})
    for simbolo in cadena:
        siguientes = mover(actuales, simbolo)
        actuales = epsilon_closure(siguientes)
    return any(estado in estados_finales for estado in actuales)


print(acepta_afn("a"))
print(acepta_afn("abba"))
print(acepta_afn(""))
print(acepta_afn("ababx"))

