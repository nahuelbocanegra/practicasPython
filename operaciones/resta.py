from operaciones import Opercaciones

class Resta(Opercaciones): #herada de operaciones
    
    def resultado(self):
        return self.get_num1() - self.get_num2()
    