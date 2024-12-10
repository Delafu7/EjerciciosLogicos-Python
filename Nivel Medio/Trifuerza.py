"""/*
 * ¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 *
 *    *
 *   ***
 *  *   *
 * *** ***
 */
"""
def trianguloTrifuerza(posiciones,num,numRestantes,altura):
        if len(posiciones[0])>num and 0<num and altura<len(posiciones):
            posiciones[altura][num]="*"
            posiciones[altura+1][num]="*"
            posiciones[altura+1][num+1]="*"
            posiciones[altura+1][num-1]="*"
            
            trianguloTrifuerza(posiciones,num-2,numRestantes-1,altura+2)
            trianguloTrifuerza(posiciones,num+2,numRestantes-1,altura+2)       
                      
def crearTrifuerza(num:int):
    if isinstance(num,int) and num>0:
        posiciones=[]
        for i in range (num*2):
            posiciones.append([])
            for _ in range((num)*3+num-1):
                posiciones[i].append(" ")
        trianguloTrifuerza(posiciones,num*2-1,num,0)
        trifuerza=""
        for i in posiciones:
            for j in i:
                  trifuerza+=j
            trifuerza+="\n"
        print(trifuerza)
        return trifuerza

crearTrifuerza(2)