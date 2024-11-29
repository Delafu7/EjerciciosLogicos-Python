"""/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */"""

def piedraPapelLagartoSpock(resultados):
    if isinstance(resultados, list) and all(len(elem)==2 for elem in resultados):
        players=[0,0]
        gana={"🗿":["✂️", "🦎" ], "✂️":["📄","🦎"], "📄":["🗿","🖖"],"🦎":["🖖","📄"],"🖖":["🗿","✂️"]}
        for parejas in resultados:
            if parejas[1] in gana[parejas[0]]:
                players[0]+=1
            elif parejas[0]==parejas[1]:
                pass
            else:
                players[1]+=1
        if players[0]>players[1]:
            return "Player 1"
        elif players[0]<players[1]:
            return "Player 2"
        else:
            return "Tie"
print(piedraPapelLagartoSpock([("🗿","✂️"), ("✂️","🦎"), ("📄","✂️")]))