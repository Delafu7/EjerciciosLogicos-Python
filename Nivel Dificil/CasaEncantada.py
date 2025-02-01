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


enigmasRespuestas=[
    {"enigma":"Cuanto más quitas, más grande es. ¿Qué es?","respuesta":"Un agujero"}, 
    {"enigma":"Me rompo si me nombras. ¿Qué soy?","respuesta":"El silencio"},
    {"enigma":"Tengo llaves pero no abro puertas. ¿Qué soy?","respuesta":"Un piano"}, 
    {"enigma":"Vuelo sin alas, lloro sin ojos. ¿Qué soy?","respuesta":"Una nube"},
    {"enigma":"Tiene dientes, pero no muerde. ¿Qué es?","respuesta":"Un peine"},
    {"enigma":"Cuanto más crece, menos se ve. ¿Qué es?","respuesta":"La oscuridad"}, 
    {"enigma":"Tiene cabeza, pero no piensa. ¿Qué es?","respuesta":"Un clavo"}, 
    {"enigma":"Es más ligero que una pluma, pero ni el hombre más fuerte lo puede sostener por mucho tiempo. ¿Qué es?","respuesta":"La respiración"},
    {"enigma":"Me ves en el agua, pero nunca me mojo. ¿Qué soy?","respuesta":"Un reflejo"},
    {"enigma":"Tengo ciudades, pero no casas; tengo montañas, pero no árboles; tengo agua, pero no peces. ¿Qué soy","respuesta":"Un mapa"},
    {"enigma":"Si me dices mi nombre, ya no existo. ¿Qué soy?","respuesta":"El secreto"},
    {"enigma":"Puedo ser alto o bajo, gordo o flaco, pero siempre miento. ¿Qué soy?","respuesta":"Un mentiroso"},
    {"enigma":"Tiene palabras, pero no habla. ¿Qué es?","respuesta":"Un libro"},
    {"enigma":"Me tiras cuando me necesitas y me recoges cuando ya no me sirvo. ¿Qué soy?","respuesta":"Un ancla"},
    {"enigma":"Cuanto más caliente estoy, más fresco te dejo. ¿Qué soy?","respuesta":"Un ventilador"},
    {"enigma":"Tengo orejas, pero no puedo oír. ¿Qué soy?","respuesta":"Una taza"},
    {"enigma":"Soy alto cuando soy joven y bajo cuando soy viejo. ¿Qué soy?","respuesta":"Una vela"},
    {"enigma":"Brilla sin ser estrella y calienta sin ser fuego. ¿Qué es?","respuesta":"El sol"},
    {"enigma":"Tiene una cabeza y una cola, pero no tiene cuerpo. ¿Qué es?","respuesta":"Una moneda"},
    {"enigma":"Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.","respuesta":"La pera"},
    {"enigma":"No es cama ni es león, y desaparece en cualquier rincón","respuesta":"El camaleón"},
    {"enigma":"Me estiras y encojo, pero nunca reviento. ¿Qué soy?","respuesta":"Un elástico"},
    {"enigma":"Todos me usan para beber, pero nadie me come. ¿Qué soy?","respuesta":"Un vaso"},{"enigma":"Cuando soy nuevo, soy alto. Cuando envejezco, me acorto. ¿Qué soy?","respuesta":"Un lápiz"}
    ]

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
    respuestasPosibles.append(enigmasRespuestas[indexEnigma].get("respuesta"))
    while len(respuestasPosibles)<4:
        respuesta=random.choice(enigmasRespuestas).get("respuesta")
        if respuesta not in respuestasPosibles:
            respuestasPosibles.append(respuesta)
    random.shuffle(respuestasPosibles)
    return respuestasPosibles

def enigmaAceptado():
    j=random.randint(0,len(enigmasRespuestas)-1)
    print("Enigma: ",enigmasRespuestas[j].get("enigma"))
    respuestasPosibles=obtenerRespuestas(j)
    for i in range(len(respuestasPosibles)):
        print(i+1,respuestasPosibles[i])
    respuesta=input("Respuesta: ")
    if respuesta.isdigit() and int(respuesta)>=1 and int(respuesta)<=4:
        respuesta=int(respuesta)-1
    else:
        raise ValueError("La respuesta debe ser un número")
    return respuestasPosibles[respuesta]== enigmasRespuestas[j].get("respuesta")

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