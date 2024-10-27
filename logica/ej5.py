"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""
def area(poligono,**kwargs):
    if poligono == "rectangulo":
        
        alto= kwargs.get("alto")
        ancho= kwargs.get("ancho")
        if alto is not None and ancho is not None:

            return alto*ancho
        
    elif poligono == "cuadrado":
        
        lado= kwargs.get("lado")
        if lado is not None:

            return lado**2
        
    elif poligono == "triangulo":
        alto= kwargs.get("alto")
        base= kwargs.get("ancho")
        
        if alto is not None and ancho is not None:

            return (base*alto)/2
