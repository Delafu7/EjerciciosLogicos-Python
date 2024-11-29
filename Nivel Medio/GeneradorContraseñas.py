"""/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */"""

import string
import random
def generadorContraseñas():
    longitud = [num for num in range(8,17)]
    valores=[chr(letra) for letra in range(ord("a"), ord("z")+1)] + [chr(letra) for letra in range(ord("A"), ord("Z")+1)] + [str(letra) for letra in range(0,10)]
    valores+= list(string.punctuation)
    patata=random.choice(longitud)
    return "".join(valor for valor in random.choices(valores,k=patata))


print(generadorContraseñas())