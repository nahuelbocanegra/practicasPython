"""
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""
def enMayuscula(cadena):
    i=0
    caracteres=""
    while i < len(cadena):

        if i == 0 or cadena[i-1] == " ":

            if cadena[i].isalpha():
                caracteres +=cadena[i].upper()
            else:
                caracteres += cadena[i]
        else:
            caracteres += cadena[i]
        i+=1
    print(caracteres)

enMayuscula(" hola como estas")
