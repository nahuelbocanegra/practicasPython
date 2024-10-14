from resta import Resta
from suma import Sumar
from dividir import Dividir
from multiplicar import Multiplicacion

objOperacion=Sumar(2,3)
objOperacion1=Resta(2,3)
objOperacion2=Dividir(2,3)
objOperacion3=Multiplicacion(2,3)


print(objOperacion.resultado())
print(objOperacion1.resultado())
print(objOperacion2.resultado())
print(objOperacion3.resultado())
