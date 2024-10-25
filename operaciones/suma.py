from operaciones import Opercaciones

class Sumar(Opercaciones):  
    
    def resultado(self):
        return self.get_num1() + self.get_num2()