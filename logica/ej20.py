"""
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
"""

def cacularMilisegundos(dias=0,horas=0,minutos=0,segundos=0):
    
    milisegundos=0

    milisegundos=dias*86400000
    milisegundos+=horas*3600000
    milisegundos+=minutos*60000
    milisegundos+=segundos*1000

    return milisegundos


print(cacularMilisegundos(1,10,10))