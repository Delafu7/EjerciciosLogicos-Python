# * Reto #6
 #* INVIRTIENDO CADENAS
 #* Fecha publicacion enunciado: 07/02/22
 #* Fecha publicacion resolucion: 14/02/22
 #* Dificultad: FACIL
 #*
 #* Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automAtica.
 #* - Si le pasamos "Hola mundo" nos retornarIa "odnum aloH"

def palabrasAlReves(phrase):
    if isinstance(phrase,str):
        return phrase[::-1]

def palabrasAlRevesMio(phrase):
    if isinstance(phrase,str):
        alReves=""
        for letra in phrase:
            alReves=letra+alReves
        return alReves
print (palabrasAlReves("Hola")) 
print (palabrasAlRevesMio("Hola"))     