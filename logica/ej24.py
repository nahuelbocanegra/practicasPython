"""
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""

def conjuntos(array1,array2,bool):

    resultado=[]
    conjuntosArray=array1+array2

    if bool == False:

        for i in conjuntosArray:
            if i in array2 and i in array1:
                continue
            resultado.append(i)

     
    if bool == True:

        for i in array1:
            if i in array2:
                resultado.append(i)

    return resultado
                


print(conjuntos([1,2,3,4],[2,4,5,6,7],True))