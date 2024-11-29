#/*
# * Implementa uno de los algoritmos de ordenación más famosos:
# * el "Quick Sort", creado por C.A.R. Hoare.
 #* - Entender el funcionamiento de los algoritmos más utilizados de la historia
 #*   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
 #*   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
 #* - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
 #*   donde trabajaremos y entenderemos los más famosos de la historia.
 #*/

def swap(lista,pos1,pos2):
    sub=lista[pos1]
    lista[pos1]=lista[pos2]
    lista[pos2]=sub
def quicksort(lista):
    if len(lista)<=1:
        return lista
    else:
        pivot=lista[len(lista)-1]
        i=0
        j=len(lista)-2
        while i<j:
            if lista[i]>pivot and lista[j]<pivot:
                swap(lista,i,j)
            if lista[i]<=pivot :
                i+=1
            if lista[j]>=pivot:
                j-=1
        if  lista[i]>lista[len(lista)-1]:
            swap(lista,i,len(lista)-1)
        else:
            swap(lista,j+1,len(lista)-1)
        lista[:j+1]=quicksort(lista[:j+1])
        lista[j+1:]=quicksort(lista[j+1:])
        return lista
    
lista= [5, 1, 2, 1, 1, 3, 5, 1, 5, 1, 99, 231, 234, 12, 121,
           312, 123, 123, 12, 312, 321, 312, 31, 23, 12, 3123, 123]
quicksort(lista)
print(lista)

#lista=[40,21,8,17,51,34]
