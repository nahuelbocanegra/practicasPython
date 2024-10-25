from operaciones import Opercaciones

class Multiplicacion(Opercaciones):

    def resultado(self):
        return self.get_num1() * self.get_num2()
    