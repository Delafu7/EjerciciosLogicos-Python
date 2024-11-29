#/*
 #* Crea un programa que calcule quien gana más partidas al piedra,
 #* papel, tijera.
 #* - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 #* - La función recibe un listado que contiene pares, representando cada jugada.
 #* - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 #*   o "S" (tijera).
 #* - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 #*/

def piedraPapelTijera(par):
    if isinstance(par,list) and all(isinstance(elem, tuple) and len(elem)==2 for elem in par):
        puntuaje=[0,0]
        for player1, player2 in par:
            if player1=="R" and player2=="P" or player1=="P" and player2=="S" or player1=="S" and player2=="R":
                puntuaje[1]+=1
            elif player2=="R" and player1=="P" or player2=="P" and player1=="S" or player2=="S" and player1=="R":
                
                puntuaje[0]+=1
        ganador=""
        if puntuaje[0]>puntuaje[1]:
            ganador="Player 1"
        elif puntuaje[1]>puntuaje[0]:
            ganador="Player 2"
        else:
            ganador="Tie"
        return ganador

