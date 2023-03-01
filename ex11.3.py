"""
Applicate la memoizzazione alla funzione di Ackermann e provate a vedere se questa 
tecnica rende possibile il calcolo della funzione con argomenti più grandi.
Suggerimento: NO.
"""

cache = {}

def ack(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ack(m-1, ack(m, n-1))
        return cache[m, n]

print(ack(3, 4))