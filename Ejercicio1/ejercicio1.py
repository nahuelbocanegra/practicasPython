"""Ejercicio 1
Escribir una clase en python que convierta un número entero a número romano"""

class Convert:
    def __init__(self):
        self.romano=[
                ("M" , 1000 ),
                ("CM", 900),
                ("D", 500),
                ("CD", 400),
                ("C" , 100),
                ("XC",90), 
                ("L" , 50),
                ("XL",40), 
                ("X" , 10),
                ("IX",9),
                ("V" , 5),
                ("V",4),
            ("I" , 1)
                ]
        
    def resultado(self,num):
        
        resultado=""
        
        for (i,j) in self.romano:
            while num >= j:
                num -= j
                resultado+=i
                
            
        return resultado


num=Convert()
print(num.resultado(1967))