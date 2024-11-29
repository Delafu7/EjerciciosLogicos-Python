#/*
 #* Crea una función que ordene y retorne una matriz de números.
 #* - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 #*   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 #*   o de mayor a menor.
 #* - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 #*   automáticamente.
 #*/

def ordenar (lista, como):
    listaOrd=[]
    if isinstance(lista,list):
        if como =="Asc":
            cont=len(lista)
            j=0
            while cont>j:
                listaOrd.append(0)
                for i in lista:
                    if listaOrd[j]==0:
                        listaOrd[j]=i
                    if i<listaOrd[j]:
                        listaOrd[j]=i
                lista.remove(listaOrd[j])
                j+=1
            return(listaOrd)
        if como =="Desc":
            cont=len(lista)
            j=0
            while cont>j:
                listaOrd.append(0)
                for i in lista:
                    if listaOrd[j]==0:
                        listaOrd[j]=i
                    if i>listaOrd[j]:
                        listaOrd[j]=i
                lista.remove(listaOrd[j])
                j+=1
            return(listaOrd)

print(ordenar([2, 4, 6, 8, 9],"Asc"))
print(ordenar([2, 4, 6, 8, 9],"Desc"))

            



