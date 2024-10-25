"""Ejercicio 2
Crea una clase “Persona”. Con atributos nombre y edad. 
Además, hay que crear un método “cumpleaños”, que aumente en 1 la edad de la 
persona cuando se invoque sobre un objeto creado con “Persona”.
Tendríamos que lograr ejecutar el siguiente código con la clase creada:"""

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def cumpleaños(self):
       self.edad+=1
      
    
    def __str__(self):
        return " mi nombre es {} y tengo {}".format(self.nombre,self.edad)
    
nahuel=Persona("nahuel",26)
nahuel.cumpleaños()
print(nahuel)

