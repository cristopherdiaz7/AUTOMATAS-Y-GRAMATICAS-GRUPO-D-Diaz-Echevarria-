
from collections import defaultdict

transiciones = defaultdict(lambda: defaultdict(list))

transiciones[0]['ε'] = [1, 6]
transiciones[1]['ε'] = [2, 4]
transiciones[2]['a'] = [3]
transiciones[4]['b'] = [5]
transiciones[3]['ε'] = [7]
transiciones[5]['ε'] = [7]
transiciones[6]['ε'] = [1]
transiciones[7]['ε'] = [6, 8]

transiciones[8]['a'] = [9]
transiciones[8]['b'] = [10]
transiciones[8]['ε'] = [11]
transiciones[9]['ε'] = [11]
transiciones[10]['ε'] = [11]

inicio = 0
final = 11

def cerradura_epsilon(estados):
    pila = list(estados)
    resultado = set(estados)
    while pila:
        estado = pila.pop()
        for destino in transiciones[estado].get('ε', []):
            if destino not in resultado:
                resultado.add(destino)
                pila.append(destino)
    return resultado

def mover(estados, simbolo):
    resultado = set()
    for estado in estados:
        for destino in transiciones[estado].get(simbolo, []):
            resultado.add(destino)
    return resultado

def acepta_afn(cadena):
    actuales = cerradura_epsilon({inicio})
    for simbolo in cadena:
        actuales = cerradura_epsilon(mover(actuales, simbolo))
    return final in actuales

print(acepta_afn("a"))
print(acepta_afn("bb"))
print(acepta_afn(""))
print(acepta_afn("abab"))
print(acepta_afn("c"))


