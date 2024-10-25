from operaciones import Opercaciones    

class Dividir(Opercaciones):
    
    def resultado(self):
        
        return self.get_num2() / self.get_num1()