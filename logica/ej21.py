"""
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
 """

import asyncio

async def sumar(num1,num2,segundos):


    await asyncio.sleep(segundos)
    return num1+num2


async def main():

    resultado1=asyncio.create_task(sumar(1,2,4))
    resultado2=asyncio.create_task(sumar(11,2,1))

    resultado_final1= await resultado1
    resultado_final2= await resultado2

    print(resultado_final1)
    print(resultado_final2)

asyncio.run(main())