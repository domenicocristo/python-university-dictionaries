"""
Scrivete una funzione che legga le parole in una lista e le inserisca come chiavi
in un dizionario. I valori non hanno importanza. Usate poi l'operatore in come modo rapido per 
controllare se una stringa è contenuta nel dizionario.
"""

def crea_dizionario(parole):
    dizionario = {}
    for parola in parole:
        dizionario[parola] = None
    return dizionario

def controlla_stringa(stringa, dizionario):
    if stringa in dizionario:
        return True
    else:
        return False

lista_parole = ["casa", "albero", "ciao", "hello"]
dizionario = crea_dizionario(lista_parole)

print(controlla_stringa("hello", dizionario))