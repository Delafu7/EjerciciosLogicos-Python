#/*
 #* Crea un programa que determine si dos vectores son ortogonales.
 #* - Los dos array deben tener la misma longitud.
 #* - Cada vector se podría representar como un array. Ejemplo: [1, -2]
 #*/

def sonVectoresOrtogonales(array1,array2):
    sonVO=False
    if len(array1) == len(array2) and isinstance(array1,list) and isinstance(array2,list) and all(isinstance(elem,int) for elem in array1) and all(isinstance(elem,int) for elem in array2):
        i=0
        while i<len(array1):
            sonVO+=array1[i]*array2[i]
            i+=1
        sonVO= sonVO==0
    return sonVO

print(sonVectoresOrtogonales([1,-2],[2,1]))