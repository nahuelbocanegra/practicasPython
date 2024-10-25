class Opercaciones:
    
    #no se puede tener dos metodos con el mismo nombre
    #self => «uno mismo»
    #metodo => acciones 
    #CONSTRUCTOR => molde del objeto

    def __init__(self,num1,num2):
        self.__num1=num1 #variable de instancia 
        self.__num2=num2
    #clase abastracta => método que no tiene una implementación, es decir, que no lleva código.
   
    def get_num1(self):
        return self.__num1

    def get_num2(self):
        return self.__num2

    def set_num1(self,num1):
        self.__num1 = num1

    def set_num2(self,num2):
         self.__num2 = num2


