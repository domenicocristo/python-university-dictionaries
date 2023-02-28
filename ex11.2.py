"""
Leggete la documentazione del metodo dei dizionari setdefault e usatelo per
scrivere una versione più concisa di inverti_dizionario.
"""

def inverti_dizionario(dizionario):
    dizionario_invertito = {}
    for chiave, valore in dizionario.items():
        dizionario_invertito.setdefault(valore, []).append(chiave)
    return dizionario_invertito

dizionario = {"h" : 1, "e"  : 1, "l" : 2, "o" : 1}
print(inverti_dizionario(dizionario))