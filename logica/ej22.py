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
import re
archivo="c:/Users/gusta/Desktop/Nahuel/Programacion 1/Python/logica/archivo.txt"

def leerArchivo(archivo):
    if os.path.exists(archivo):
        with open(archivo,"r") as file:
            contenido = file.read()   
    else:
        print("el archivo no existe")
    
    return contenido

def lista():

    contenido=leerArchivo(archivo)

    #EXPRESIONES REGULARES 
    resultado_lista=re.findall(r'\d+|[+\-*/()]', contenido) 
    #captura numeros y operadores matematicos
    

    return resultado_lista
    
 

def total(res):

    for i in res:
        if i == "*":
            mul=int(res[res.index(i)-1])*int(res[res.index(i)+1])
            del res[res.index(i)-1]
            del res[res.index(i)+1]
            res[res.index(i)] = mul
            
         
        elif i == "/":
            div=int(res[res.index(i)-1])//int(res[res.index(i)+1])
            del res[res.index(i)-1]
            del res[res.index(i)+1]
            res[res.index(i)] = div
          
   
    for i in res:
        for j in res:
            if j == "+":
                sum=int(res[res.index(j)-1])+int(res[res.index(j)+1])
                del res[res.index(j)-1]
                del res[res.index(j)+1]
                res[res.index(j)] = sum  
            elif j  == "-":
                resta=int(res[res.index(j)-1]) - int(res[res.index(j)+1])
                del res[res.index(j)-1]
                del res[res.index(j)+1]
                res[res.index(j)] = resta
           
        
        
     
        
    return res[0]


resultado_lista=lista()

print(total(resultado_lista))




