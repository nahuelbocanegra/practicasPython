"""
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
"""

def armstrong(num):

    digito_array=[int(digito) for digito in str(num)]
    resultado=0
    
    for i in digito_array :
        resultado+= i**3

    if num == resultado: return True

    return False

print(armstrong(1234))