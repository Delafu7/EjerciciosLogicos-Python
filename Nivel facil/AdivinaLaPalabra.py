"""/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */"""

import random
def juegoAdivinaPalabras():
    lPalabras=["chorizo","patata"]
    maxOcultacion=random.choice([elem for elem in range(1, int(len(lPalabras[0])*0.6))])
    palabra=random.choice(lPalabras)
    palabraOculta=palabra
    lista=[num for num in range(0,len(palabra))]
    contAAcertar=0 
    numIntentos=3
    posiciones=[]
    for _ in range (maxOcultacion,0,-1):
        letra=random.choice(lista)
        palabraOculta= palabraOculta[:letra]+"_"+palabraOculta[letra+1:]
        posiciones.append(letra)
        contAAcertar+=1
        lista.remove(letra)
    while numIntentos>0 and contAAcertar>0 :
        print(palabraOculta)
        valor=input("Introduce la letra que creas que puede aparecer en el sistema\n").strip()
        contAAcertarInicial=contAAcertar
        if(len(valor)>0):
            for posicion in posiciones:
                if (valor==palabra[posicion]):
                    print("Acertaste\n")
                    palabraOculta=palabraOculta[:posicion]+valor[0]+palabraOculta[posicion+1:]
                    contAAcertar-=1
        if contAAcertar==contAAcertarInicial:
            print("Fallaste\n")
            numIntentos-=1
    print(palabraOculta)
juegoAdivinaPalabras()
    

