"""/*
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */"""

import random

enigmas=["¿Qué es lo que tiene ojos y no puede ver?","¿Qué es lo que tiene dientes y no puede comer?","¿Qué es lo que tiene cabeza y no puede pensar?","¿Qué es lo que tiene corazón y no puede amar?"]
respuestas=["una aguja","un peine","un huevo","un reloj"]

def mostrarCasa(num:int,puerta:int,dulces:int,iPersona:int,jPersona:int):
    casa=[]
    for i in range(num):
        casa.append([])
        for j in range(num):
            if i==0 and j==puerta:
                casa[i].append("🚪")
            elif i==num-1 and j==dulces:
                casa[i].append("🍭")
            elif i==iPersona and j==jPersona:
                casa[i].append("🧍")
            else:
                casa[i].append("⬜️")
    casaStr=""
    for i in range(len(casa)):
        for j in range(len(casa[i])):
            casaStr+=casa[i][j]
        casaStr+="\n"
    print(casaStr)

def obtenerRespuestas(indexEnigma:int):
    respuestasPosibles=[]
    respuestasPosibles.append(respuestas[indexEnigma])
    while len(respuestasPosibles)<4:
        respuesta=random.choice(respuestas)
        if respuesta not in respuestasPosibles:
            respuestasPosibles.append(respuesta)
    random.shuffle(respuestasPosibles)
    return respuestasPosibles

def enigmaAceptado():
    j=random.randint(0,len(enigmas)-1)
    print("Enigma: ",enigmas[j])
    respuestasPosibles=obtenerRespuestas(j)
    for i in range(len(respuestasPosibles)):
        print(i+1,respuestasPosibles[i])
    respuesta=input("Respuesta: ")
    if respuesta.isdigit() and int(respuesta)>=1 and int(respuesta)<=4:
        respuesta=int(respuesta)-1
    else:
        raise ValueError("La respuesta debe ser un número")
    return respuestasPosibles[respuesta]==respuestas[j]

def juegoCasaEncantada(num:int=4):
    print("Bienvenido a la casa encantada")
    terminar=False
    puerta=random.randint(0,num-1)
    dulces=random.randint(0,num-1)  
    j=0
    i=puerta
    mostrarCasa(num,puerta,dulces,j,i)
    while not terminar:
        if j==num-1 and i==dulces:
            print("Felicidades encontraste los dulces")
            print("LLegaste a la salida")
            terminar=True
        else:
           
            if enigmaAceptado():
                print("Respuesta correcta")
                valor=random.randint(0,10)
                if valor<=1:
                    print("Aparecieron fantasmas")
                if valor>1 or (valor<=1 and enigmaAceptado()):
                    if valor<=1:
                        print("Respuesta correcta de fantasmas")
                    indexI=i
                    indexJ=j
                    while indexI==i and indexJ==j:
                        print("Hacia donde quieres moverte: norte/sur/este/oeste")
                        movimiento=input()
                        if movimiento=="norte" and j>0:
                            j-=1
                        elif movimiento=="sur" and j<num-1:
                            j+=1
                        elif movimiento=="este" and i<num-1:
                            i+=1
                        elif movimiento=="oeste" and i>0:
                            i-=1
                        else:
                            print("Movimiento no permitido")
                    mostrarCasa(num,puerta,dulces,j,i)
                else:
                    print("Respuesta incorrecta de fantasmas")
            else:
                print("Respuesta incorrecta")
juegoCasaEncantada()