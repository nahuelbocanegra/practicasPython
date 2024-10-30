"""
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
"""

def eliminandocaracteres(str1,str2):

    
    out1=""
    out2=""

    for i in str1:
        if i in str2:
            out2=str1.replace(i,"")
            out1=str2.replace(i,"")
    

                
    print(out2)
    print(out1)



eliminandocaracteres("hola","juan")