"""
Se avete svolto l'Esercizio 10.7, avrete già una funzione di nome ha_duplicati
che richiede come parametro una lista e restituisce True se ci sono oggetti ripetuti 
all'interno della lista.
Usate un dizionari per scrivere una versione più rapida e semplice di ha_duplicati.
"""

def ha_duplicati(d):
    values_set = set()
    for value in d.values():
        if value in values_set:
            return True
        values_set.add(value)
    return False

d1 = {1: "hello", 2: "world", 3: "hello"}
print(ha_duplicati(d1))

d2 = {1: "hello", 2: "world", 3: "!"}
print(ha_duplicati(d2))  