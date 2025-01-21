"""/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */"""
import random as r

def calcularClima(dias:int,temperatura:int,probLluvia:int)->None:
    tempMax=temperatura
    tempMin=temperatura
    diasLluvia=0
    for i in range(dias):
        if r.randint(0,100)<10:
            temperatura+=2 if r.randint(0,1) else -2
        if temperatura>25:
            probLluvia+=20
        if temperatura<5:
            probLluvia-=20
        if r.randint(0,100)<probLluvia:
            temperatura-=1
            diasLluvia+=1
        if temperatura>tempMax:
            tempMax=temperatura
        if temperatura<tempMin:
            tempMin=temperatura
        print(f"El día {i+1} la temperatura es de {temperatura}°C")	
    print(f"La temperatura máxima fue de {tempMax}°C")
    print(f"La temperatura mínima fue de {tempMin}°C")
    print(f"Hubo lluvia {diasLluvia} días")
calcularClima(5,20,50)