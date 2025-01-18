"""/*
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)
 */"""

def sumas(lista:list, vObjetivo:int)->list:
    if isinstance(lista,list) and isinstance(vObjetivo,int):
        if lista==[]:
            return []
        else:
            propuestas=[]
            for i in range(len(lista)):
                suma=lista[i]
                posible=[lista[i]]
                for j in range(i+1,len(lista)):
                    if suma+lista[j]<=vObjetivo:
                        suma+=lista[j]
                        posible.append(lista[j])
                        if suma==vObjetivo:
                            suma=lista[i]
                            propuestas.append(posible)
                            posible=[lista[i]]	
                    else:
                        posible=[lista[i]]
                        suma=lista[i]
            return propuestas
    else:
        return []
print(sumas([1, 5, 3, 2], 6)) # [1, 5], [1, 3, 2]
print(sumas([1, 5, 3, 2], 7)) # [5, 2]
print(sumas([1, 5, 3, 2,3], 8)) # [5, 3], [3, 2, 3]
print(sumas([1, 5, 3, 2], 11)) # []
print(sumas([], 6)) # []
print(sumas([1, 5, 3, 2], 0)) # []
