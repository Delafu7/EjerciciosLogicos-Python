"""/*
 * Dado un array de números enteros positivos, donde cada uno
 * representa unidades de bloques apilados, debemos calcular cuantas unidades
 * de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *          ⏹
 *          ⏹
 *   ⏹💧💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
 *   de agua. Suponemos que existe un suelo impermeable en la parte inferior
 *   que retiene el agua.
 */"""

from queue import Queue

def agua_atrapada(bloques, numGotas):
    columnas = []
    maxBloque=0
    for bloque in bloques:
        fila=Queue(bloque)
        for _ in range(bloque):
            fila.put("⏹︎")
        columnas.append(list(fila.queue))
        if maxBloque<bloque:
            maxBloque=bloque
    for _ in range(numGotas):
        i=1
        enc=False
        menor=len(columnas[0])
        ident=0
        while  i <len(bloques) and not enc:   
            if len(columnas[i])==0:
                enc=True
                ident=i
            elif len(columnas[i])<menor:
                menor=len(columnas[i])
                ident=i
            i+=1
        columnas[ident].append("💧")
    mostrar=""
    for i in range(maxBloque-1,-1,-1):
        for columna in columnas:
            if len(columna)-1<i:
                mostrar=mostrar+ "   " 
            else:
                mostrar=  mostrar + f" {columna[i]} "
        mostrar=mostrar+"\n"
    print(columnas)
    return mostrar
print(agua_atrapada([4, 0, 3, 6, 1, 3],7))

