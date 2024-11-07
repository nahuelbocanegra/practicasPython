"""
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""
 
def palindromo(cadena):
   
   cadena_reverse=cadena[::-1].upper().split()
   cadena_reverse="".join(cadena_reverse)

   cadena=cadena.upper().split()
   cadena="".join(cadena)
   
   return cadena_reverse==cadena

        


palindromo("ana lleva al ooso la avellana")
