"""
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
"""
 

morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    }
morse_code_reversed={v:k for k,v in morse_code.items()}

def conversion_morse(cadena):
    cadena=cadena.upper()
    mensaje=""

    for i in cadena:
        if i in morse_code.keys():
            mensaje += morse_code[i] + " "
        if i == " ":
            mensaje+="  "
    return mensaje

def conversion_texto(cadena):
    array_cadena= cadena.split(" ")
    mensaje=""
    for i in array_cadena:
        if i in morse_code_reversed.keys():
            mensaje += morse_code_reversed[i] 
        
    return mensaje   

def conversion(cadena):
    if all(x in [".","-"," "] for x in cadena):
       return conversion_texto(cadena).strip()
    else:
       return conversion_morse(cadena).strip()
        
print(conversion(".... --- .-.. .-   -.-. --- -- ---   . ... - .- ... "))
print(conversion("HOLA COMO ESTAS"))

     
    
  
            