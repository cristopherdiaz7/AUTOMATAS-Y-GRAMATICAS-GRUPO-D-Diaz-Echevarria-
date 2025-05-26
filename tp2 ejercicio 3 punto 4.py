AFD = {
    'A': {'a': 'A', 'b': 'A'}
}

estado_inicial = 'A'
estado_final = {'A'}

def acepta_afd(cadena):
    estado_actual = estado_inicial
    for simbolo in cadena:
        if simbolo not in AFD[estado_actual]:
            return False
        estado_actual = AFD[estado_actual][simbolo]
    return estado_actual in estado_final

print(acepta_afd(""))
print(acepta_afd("a"))
print(acepta_afd("bbba"))
print(acepta_afd("babab"))
print(acepta_afd("c"))

