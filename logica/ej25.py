"""
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""
def maximoComunDivisor(num1,num2):

    mcdnum1={}
    i=2
    while num1>0: 
        if num1 % i == 0:
            num1=num1//i
            print(num1)
            i-1
        i+1
        print(i)
    
    return num1

maximoComunDivisor(100,100)

