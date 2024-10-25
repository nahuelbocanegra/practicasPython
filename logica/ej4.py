"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""
def primo(num):
    cantidad=0
    for i in range(1,101):
        if num%i == 0:
            cantidad+=1

    if cantidad>2:
        return "no es primo"       
    return "es primo"

print(primo(13))