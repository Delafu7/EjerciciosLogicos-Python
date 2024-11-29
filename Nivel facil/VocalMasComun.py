"""/*
 * Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
 */"""

import unicodedata
def quitarTildes(texto:str):
    texto_normalizado=unicodedata.normalize("NFD",texto)
    texto_sinTildes="".join(caracter for caracter in texto_normalizado if unicodedata.category(caracter) !="Mn")
    return unicodedata.normalize("NFC",texto_sinTildes)
def vocal_mas_repetida(texto):
    if isinstance(texto,str):
        texto = texto.lower()
        vocales="aueio"
        texto=quitarTildes(texto)
        max_repetidas = 0
        vocal_max_repetida= ""
        for vocal in vocales:
            contador = texto.count(vocal)
            if contador > max_repetidas:
                max_repetidas = contador
                vocal_max_repetida = vocal
        return vocal_max_repetida,max_repetidas
print(vocal_mas_repetida(" Si no hay vocales podrá devolver vacío."))