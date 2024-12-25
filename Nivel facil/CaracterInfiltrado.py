"""/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres.
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 *
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */
 """

class DistintaLongitudError(Exception):
    """Excepción para cuando las cadenas no tienen la misma longitud"""
    pass

def encontrarCaracterInfiltrado(cadena1:str, cadena2:str)->list:
   try:
        if len(cadena1)!=len(cadena2):
            raise DistintaLongitudError("Las cadenas no tienen la misma longitud")
        return [ cadena2[i] for i in range (len(cadena2)) if cadena1[i]!=cadena2[i] ]
   except DistintaLongitudError as e:
         return e

print(encontrarCaracterInfiltrado("Me llamo mouredev", "Me llemo mouredov"))
print(encontrarCaracterInfiltrado("Me llamo.Brais Moure", "Me llamo brais moure"))
print(encontrarCaracterInfiltrado("Me llamo.Brais Mour", "Me llamo brais moure"))