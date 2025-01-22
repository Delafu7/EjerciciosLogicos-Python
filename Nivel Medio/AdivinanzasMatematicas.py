"""/*
 * Crea un juego interactivo por terminal en el que tendrás que adivinar
 * el resultado de diferentes operaciones matemáticas aleatorias
 * (suma, resta, multiplicación o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 *   ..
 */"""
import random
import time


def adivinanzasMatematicas():
    lNumeros=[0,1,2,3,4,5,6,7,8,9]
    lOperaciones=["+","-","*","/"]
    aciertos=0
    terminar=False
    while not terminar:
        numero1=""
        numero2=""
        if aciertos%5==0:
             if aciertos==0:
                 cifras=1
             else:
                 cifras+=1
        for _ in range(cifras):
             numero1+=str(random.choice(lNumeros))
             numero2+=str(random.choice(lNumeros))
        operacion=random.choice(lOperaciones)

        if operacion=="+":
            resultado=int(numero1)+int(numero2)
        elif operacion=="-":
            resultado=int(numero1)-int(numero2)
        elif operacion=="*":
            resultado=int(numero1)*int(numero2)
        else:
            if int(numero2)==0:
                numero2=1   
            resultado=int(numero1)/int(numero2)
        print(f"{numero1} {operacion} {numero2}")
        print("Tienes 3 segundos para responder")
        print(resultado)
        tiempoInicial=time.time() 
        respuesta=input("Respuesta: ")
        tiempoFinal=time.time()
        if tiempoFinal-tiempoInicial>3:
            print("Tiempo agotado")
            terminar=True
        elif int(respuesta)==int(resultado):
            aciertos+=1
            print("Correcto")
        else:
            print("Incorrecto")
            terminar=True
    print(f"Has acertado {aciertos} cálculos")
adivinanzasMatematicas()