#/*
# * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 #* y retorne su resultado en milisegundos.
# */

from datetime import timedelta

def calcularMiliseconds(dias, horas, mins, segs):
    if all(isinstance(i, int) for i in [dias,horas,mins,segs]):
        tiempo= timedelta(days=dias,hours=horas,minutes=mins, seconds=segs)
        return (int(tiempo.total_seconds()*1000))


    