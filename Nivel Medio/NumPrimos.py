# * Reto #3
 #* ES UN NUMERO PRIMO?
 #* Fecha publicacion enunciado: 17/01/22
 #* Fecha publicacion resolucion: 24/01/22
 #* Dificultad: MEDIA
 #*
 #* Enunciado: Escribe un programa que se encargue de comprobar si un numero es o no primo.
 #* Hecho esto, imprime los numeros primos entre 1 y 100.
 #*

def isPrime(num):
    correct=True
    if num%2==0 and num!=2:
        correct=False
    if num%3==0 and num!=3:
        correct=False
    if num%5==0 and num!=5:
        correct=False
    if num%7==0 and num!=7:
        correct=False
    return correct
        


def generarPrimos(numInic, numFin):
    for i in range(numInic,numFin+1):
        if isPrime(i):
            print(i)

generarPrimos(1,100)
