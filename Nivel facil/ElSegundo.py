#/#*
 #* Dado un listado de números, encuentra el SEGUNDO más grande
 #*/


def listadoNumeros(lista):
    if isinstance(lista,list) and all(isinstance(elem,int) for elem in lista):
        contMax=[0,0]
        for i in lista:
            if i>contMax[0]:
                if contMax[0]>=contMax[1]:
                    contMax[1]=contMax[0]
                contMax[0]= i
            elif i>contMax[1]:
                if contMax[1]>=contMax[0]:
                    contMax[0]=contMax[1]
                contMax[1]=i
        if contMax[0]>contMax[1]:
            return contMax[1]
        else:
            return contMax[0]
    
print(listadoNumeros([4, 6, 1, 8, 2]))
print(listadoNumeros([4, 6, 8, 8, 6]))
print(listadoNumeros([4, 4]))
print(listadoNumeros([]))