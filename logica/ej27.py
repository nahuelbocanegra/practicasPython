"""
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
"""
 
def dibujarCuadrado(lado):
    dibujo=""
    for i in range(lado):
        for j in range(lado):
            dibujo+="* "
        dibujo+="\n"

    print(dibujo)
dibujarCuadrado(4)

def dibujarRectangulo(base,altura):
    dibujo=""
    for i in range(base):
        for j in range(altura):
            dibujo+="* "
        dibujo+="\n"

    print(dibujo)
dibujarRectangulo(4,5)

