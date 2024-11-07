"""
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
"""

def contarConFor():
    for i in range(1,101):
        print(i)

contarConFor()

def contarConWhile():
    i=1
    while i < 101:
        print(i)
        i+=1

contarConWhile()

def contarConRecurion(n):
    print(n)
    if n < 100:
        contarConRecurion(n+1)
    

contarConRecurion(1)
        