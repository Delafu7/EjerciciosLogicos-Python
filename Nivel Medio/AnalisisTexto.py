"""/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */"""

import re

def analizar_texto(texto:str):
    palabras = texto.lower().split()
    longMedia=0
    numOraciones=0
    palabraMasLarga=""
    numTotPalabras=0
    for palabra in palabras:
        cont=0
        numTotPalabras+=1
        for letra in palabra:
            if letra == ".":
                numOraciones+=1
            elif re.search(r'[a-z]',letra):
                cont+=1
        if cont>len(palabraMasLarga):
            palabraMasLarga=palabra
        longMedia+=cont
        
    return f" - Número total de palabras: {numTotPalabras} \n - Longitud media de las palabras: {longMedia/numTotPalabras}\n - Número de oraciones del texto (cada vez que aparecen un punto): {numOraciones}\n - Encuentre la palabra más larga: {palabraMasLarga}\n"

print(analizar_texto("Hola, mundo. Esto es un texto. Para analizar."))