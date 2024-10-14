class Opercaciones:
    
    #no se puede tener dos metodos con el mismo nombre
    
    #CONSTRUCTOR
    def __init__(self,num1,num2):
        self.num1=num1 #variable de instancia 
        self.num2=num2
    
    #self => «uno mismo»
    def sumar(self):
        return self.num1 + self.num2
    #metodo => acciones 
    def resta(self):
        return self.num1 - self.num2
    

class Operaciones2:
    def saludar(self):
        return "Hola mundo"