from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido,carrera):
        super().__init__(nombre, apellido)
        self.carrera=carrera

    def mostrar_carrera(self):
        return "el estudante {} {}, esta cursando la carrara de {}"\
            .format(self.nombre,self.apellido,self.carrera)
    