#/*
 #* Crea una función que imprima los 30 próximos años bisiestos
 #* siguientes a uno dado.
 #* - Utiliza el menor número de líneas para resolver el ejercicio.
 #*/
from datetime import date
def proximosAñosBisiestos(cuantos):
    fechaActual=date.today().year+1
    while 0<cuantos:
        if (fechaActual%4==0 and fechaActual%100!=0) or (fechaActual%4==0 and fechaActual%100==0 and fechaActual%400==0): 
            print(fechaActual)
            cuantos-=1
        fechaActual+=1
proximosAñosBisiestos(30)

def proximosAñosBisiPython(cuantos):
    print([anno for anno in (date.today().year+1,date.today().year+cuantos*5) if (anno%4==0 and anno%100!=0) or (anno%4==0 and anno%100==0 and anno%400==0)][:cuantos])

proximosAñosBisiPython(30)