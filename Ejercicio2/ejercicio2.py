"""Realizar un programa que conste de una clase llamada Estudiante, q
ue tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar
un mensaje con el resultado de la nota y si ha aprobado o no."""

class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def __str__(self):#El método __str__ devuelve una cadena que describe el objeto de forma legible
        return "el alumno {} tiene una nota {}".format(self.nombre,self.nota)
    
    def resultado(self):
        if self.nota >= 6:
            return "aprobado"
        return "desaprobado"
        

nahuel=Estudiante("NAHUEL",6)
print(nahuel.resultado())
print(nahuel)# Llama automáticamente a persona.__str__()