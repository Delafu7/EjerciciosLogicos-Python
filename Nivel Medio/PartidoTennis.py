"""/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */"""

def partidoTenis(resultado:list):
    if isinstance(resultado,list) and all(elem for elem in resultado if elem=="P1" or elem=="P2") :
        puntos = ["Love", 15, 30, 40, "Ventaja"]
        puntJ1=0
        puntJ2=0
        for set in resultado:
            if set == "P1":
                puntJ1+=1
            else:
                puntJ2+=1
            if puntJ1==len(puntos):
                print("Ha ganado el P1")
                return
            elif puntJ2==len(puntos):
                print("Ha ganado el P2")
                return
            elif puntos[puntJ1]=="ventaja" and set =="P2":
                puntJ1-=1
                if len(puntos)-1==puntJ2:
                    puntJ2-=1
                else:
                    puntJ2+=1
            elif puntos[puntJ2]=="ventaja" and set =="P1":
                puntJ2-=1
                if len(puntos)-1==puntJ1:
                    puntJ1-=1
                else:
                    puntJ1+=1
            else:
                if puntJ1==len(puntos)-1:
                    print("Ventaja P1")
                elif puntJ2==len(puntos)-1:
                    print("Ventaja P2")
                else: 
                    print("Deuce" if puntJ1==puntJ2 and puntos[puntJ1]==40 else f"{str(puntos[puntJ1])} - {str(puntos[puntJ2])}")
partidoTenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])

