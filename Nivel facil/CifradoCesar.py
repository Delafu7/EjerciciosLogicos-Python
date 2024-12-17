"""/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */"""

print(ord("a"),ord("z"),ord("A"),ord("Z"))
def cifradoCesar(mensaje:str,rotacion)->str:
    cifrado=""
    for letra in mensaje:
        if letra.isalpha():
            orden=ord(letra)
            orden+=rotacion
            if letra.islower() and orden>122:
                    orden=orden-122+96
            elif letra.isupper() and orden>90:
                    orden=orden-90+64
            cifrado+=chr(orden)
        else:
            cifrado+=letra
    return cifrado

def descifradoCesar(mensaje:str,rotacion)->str:
    cifrado=""
    for letra in mensaje:
        if letra.isalpha():
            orden=ord(letra)
            orden-=rotacion
            if letra.islower() and orden<97:
                    orden=123-(97-orden)
            elif letra.isupper() and orden<65:
                    orden=91-(65-orden)
            cifrado+=chr(orden)
        else:
            cifrado+=letra
    return cifrado
print(cifradoCesar("hola",13))
print(cifradoCesar("HOLA",13))
print(descifradoCesar("ubyn",13))
print(descifradoCesar("UBYN",13))
    
                