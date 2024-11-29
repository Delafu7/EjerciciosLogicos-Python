"""/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */"""

def heterograma(texto:str) -> bool:
    """Un heterograma es una palabra o frase en la que cada letra aparece una vez"""
    return all(texto.count(letra)==1 for letra in texto)

def isograma(texto:str)->bool:
    """Un isograma es una palabra o frase en la que no hay letras repetidas"""
    setter=set(texto.lower())
    cont=texto.count(list(setter)[0])
    return all(texto.count(letra)==cont for letra in setter)

def pangrama(texto:str)->bool:
    """Un pangrama es una frase que contiene todas las letras del alfabeto"""
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    return all(letra in texto.lower() for letra in alfabeto)

def heteroIsoPangrama(texto:str):
    fras="texto"
    if heterograma(texto):
        fras+=" es heterograma, "
    else:
        fras+="no es heterograma, "
    if isograma(texto):
        fras+=" es isograma, "
    else:
        fras+="no es isograma, "
    if pangrama(texto):
        fras+=" es pangrama."
    else:
        fras+="no es pangrama."
    return fras
print(heterograma("murcielago"))
print(isograma("dandandan"))
print(pangrama("La casa de los abuelos"))
print(heteroIsoPangrama("The quick brown fox jumps over the lazy dog"))
print(heteroIsoPangrama("La casa de los abuelos"))