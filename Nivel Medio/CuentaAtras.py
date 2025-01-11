"""/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */"""
import time
def cuentaAtras(numComienzo, segundosTranscurso):
   
    if isinstance(numComienzo,int) and isinstance(segundosTranscurso,int):
        tiempo=numComienzo
        cuenta=1
        cont=0
        while tiempo>0:
            print(f"Tiene un tiempo de {tiempo} en la cuenta {cuenta}")
            tiempo-=1
            time.sleep(1)
            cont+=1
            if cont==segundosTranscurso or segundosTranscurso==0:
                cont=0
                cuenta+=1
    else:
        print("Parametro incorrecto")
        raise ValueError
    
             
cuentaAtras(4,1)