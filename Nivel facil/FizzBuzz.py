#/*
 #* Reto #0
 #*# EL FAMOSO "FIZZ BUZZ"
 #* Fecha publicacion enunciado: 27/12/21
 #* Fecha publicacion resolucion: 03/01/22
 #* Dificultad: FACIL
 #* Enunciado: Escribe un programa que muestre por consola (con un print) los numeros de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresion), sustituyendo los siguientes:
 #* - Multiplos de 3 por la palabra "fizz".
 #* - Multiplos de 5 por la palabra "buzz".
 #* - Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 #*

def fizzBuzz():
    for i in range (1,101):
        palabra=""
        if i%3==0:
            palabra+="fizz"
        if i%5==0:
            palabra+="buzz"
        print("Number: "+str(i)+" number asociate with the word: "+palabra+"\n")
fizzBuzz()