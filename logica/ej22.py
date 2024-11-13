"""
 * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 * resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un
 *   símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 *   y división "/".
 * - El resultado se muestra al finalizar la lectura de la última
 *   línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han
 *   podido resolver las operaciones.
"""
import os
archivo="c:/Users/gusta/Desktop/Nahuel/Programacion 1/Python/logica/archivo.txt"

def leerArchivo(archivo):
    if os.path.exists(archivo):
        with open(archivo,"r") as file:
            contenido = file.read()   
    else:
        print("el archivo no existe")
    
    return contenido

def resultado(archivo):

    contenido=leerArchivo(archivo)

    resultadoString=[]

    for i in contenido:
        if i == "\n":
            continue
        resultadoString.append(i)

    resultadoEntero=0

    for i in resultadoString:
       if i.isdigit():
           resultadoEntero=i

    

    print(resultadoString)


resultado(archivo)
""""
for i in contenido:
    if i == "\n":
        continue
    if i == "+":
        resultado+=i
    resultado=i
print(resultado)
"""


