"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def Abinario(num):
    binario=""
    for i in range(num):
       
        binario+=f"{num%2}"
        num=num//2
      
        if num<=0:
            break

    return binario[::-1]
      

   

num=302
print(Abinario(num))

