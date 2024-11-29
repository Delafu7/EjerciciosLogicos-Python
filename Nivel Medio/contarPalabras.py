#* Crea un programa que cuente cuantas veces se repite cada palabra
 #* y que muestre el recuento final de todas ellas.
 #* - Los signos de puntuacion no forman parte de la palabra.
 #* - Una palabra es la misma aunque aparezca en mayusculas y minusculas.
 #* - No se pueden utilizar funciones propias del lenguaje que
 #*   lo resuelvan automaticamente.

def contar_palabras(texto):
    nuevoTexto = texto.lower()
    palabras = nuevoTexto.split()
    recuento = {}
    for palabra in palabras:
        palabra= ''.join([caracter for caracter in palabra if caracter.isalnum()])
        if palabra in recuento:
            recuento[palabra]+=1
        else:
            
            recuento[palabra]=1
    return recuento

print(contar_palabras("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev)."))


#Este codigo genera una lista de caracteres, 
# pero solo annade aquellos que cumplan con la condicion caracter.isalnum(). 
# La funcion isalnum() devuelve True si el caracter es alfanumerico
#  (es decir, si es una letra o un numero).

import re 
def contar_palabras2(texto):
    nuevoTexto = texto.lower()
    palabras = nuevoTexto.split()
    recuento = {}
    for palabra in palabras:
    
        palabra= re.sub(r'[^a-zA-Z0-9]','',palabra)
        if palabra in recuento:
            recuento[palabra]+=1
        else:
            
            recuento[palabra]=1
    return recuento

print(contar_palabras2("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev)."))

#re.sub(pattern, replacement, string):
#Esta funcion reemplaza todas las coincidencias del patron dado por el texto
#  de reemplazo en la cadena original.

#El patron r'[^a-zA-Z0-9]':
#Aqui [^a-zA-Z0-9] significa "cualquier caracter que no sea una letra 
# (minuscula o mayuscula) o un numero".
#  La ^ dentro de los corchetes niega el conjunto,
#  por lo que selecciona cualquier caracter que no sea alfanumerico.

#Reemplazo por una cadena vacia '':
#Cuando se encuentra un caracter que no es alfanumerico, 
# se reemplaza por una cadena vacia, eliminandolo efectivamente.