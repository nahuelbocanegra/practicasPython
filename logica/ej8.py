"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 """

def palabrasRepetidas(texto):

    signos_puntuacion = ".,;:!?()[]{}\"'"

    # Limpiar el texto y convertirlo a minúsculas
    for caracter in signos_puntuacion:
        texto = texto.replace(caracter, '')

    repetidas={}
    array_palabras=texto.lower().split(" ")
    
    
  
    for i in array_palabras:
        if i not in repetidas:
            repetidas[i]=1
        else:
           repetidas[i] +=1
        
    return repetidas


mensaje="hola, hola hola como estas"

print(palabrasRepetidas(mensaje))