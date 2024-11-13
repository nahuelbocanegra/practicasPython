"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

def PiedraPapelTijera(jugadas):

    player1=0
    player2=0

    for i in jugadas:
        print(i)
        if i[0] == i[1]:
          continue
        elif i[0] == "S" and i[1] == "P" or i[0] == "R" and i[1] == "S" or i[0] == "P" and i[1] == "S"  :
           player1 +=1
        else:
           player2 +=1
           
           

    if player1 == player2:
        return "Tie"
    elif player1 > player2:
        return "Player1"
    else: 
       return "Player2"

print(PiedraPapelTijera([("R","S"), ("S","R"), ("P","S")]))