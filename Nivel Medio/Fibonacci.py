# * Enunciado: Escribe un programa que imprima los 50 primeros numeros de la sucesion de Fibonacci empezando en 0.
 #* La serie Fibonacci se compone por una sucesion de numeros en la que el siguiente siempre es la suma de los dos anteriores.
 #* 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(num):
    first,second=0,1
    for i in range(num+1):
        print("La secuencia de num "+str(i)+ ": "+str(first))
        aux=first
        first=second
        second=second+aux

fibonacci(50)

#De forma recursiva.
def fibonacci_recu(first,second, cont,num):
    if cont>num:
        return
    else:
        aux=second
        second+=first
        print("La secuencia de num "+str(cont)+ ": "+str(first)) 
        cont+=1
        fibonacci_recu(aux,second,cont,num)
def sec_fibonacci(num):
    cont=0
    fibonacci_recu(0,1,0,num)
sec_fibonacci(50)
