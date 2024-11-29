#/*
# * Crea un programa que calcule el daño de un ataque durante
 #* una batalla Pokémon.
 #* - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 #* - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 #* - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 #*   (buscar su efectividad)
 #* - El programa recibe los siguientes parámetros:
 #*  - Tipo del Pokémon atacante.
 #*  - Tipo del Pokémon defensor.
 #*  - Ataque: Entre 1 y 100.
 #*  - Defensa: Entre 1 y 100.
 #*/

def dannoAtaquePokemon(tipoPAtack,tipoPDefend, ataque,defensa):
    if isinstance(tipoPAtack,str) and tipoPAtack in ["Agua","Fuego","Planta","Eléctrico"] and isinstance(tipoPDefend,str) and tipoPDefend in ["Agua","Fuego","Planta","Eléctrico"] and (isinstance(ataque,float) and isinstance(defensa,float) or isinstance(ataque,int) and isinstance(defensa,int) )  :
        efectividad=1
        if(tipoPAtack=="Agua" and tipoPDefend=="Fuego") or (tipoPAtack=="Fuego" and tipoPDefend=="Planta") or (tipoPAtack=="Planta" and tipoPDefend=="Agua") or (tipoPAtack=="Eléctrico" and tipoPDefend=="Agua"):
            efectividad=2
        elif (tipoPAtack==tipoPDefend) or (tipoPAtack=="Agua" and tipoPDefend=="Planta") or (tipoPAtack=="Fuego" and tipoPDefend=="Agua") or (tipoPAtack=="Planta" and tipoPDefend=="Fuego") or (tipoPAtack=="Eléctrico" and tipoPDefend=="Planta"):
            efectividad=0.5
        return 50*(ataque/defensa)*efectividad
    
print(dannoAtaquePokemon("Agua","Fuego", 32,50))
