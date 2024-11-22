"""
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
"""

def ordenar(array,orden,nuevoArray):

    if len(array)==0:
        return nuevoArray

    if orden == "Desc":
        mayor = float('-inf')
        for i in array:
            if i > mayor:
                mayor=i

        array.remove(mayor)     
        nuevoArray.append(mayor)    


    elif orden == "Asc":
        menor=  float("inf")
        for i in array:
            if i < menor:
                menor=i
        array.remove(menor)     
        nuevoArray.append(menor)


    return ordenar(array,orden,nuevoArray)

resultado=ordenar([2, 6, 1, 3, 9],"Asc",[])
resultado1=ordenar([2, 6, 1, 3, 9],"Desc",[])

print(resultado)
print(resultado1)
