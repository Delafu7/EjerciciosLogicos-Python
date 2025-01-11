"""/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / %
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */"""

def esExpresionMatematica(expresion:str)->bool:
    if isinstance(expresion,str):
        expresion=expresion.split()
        esEM=True
        siguienteValor=False
        i=0
        while i<len(expresion) and esEM:
            if expresion[i] in ["+","-","*","/","%"]:
                if i!=0 and not(expresion[i-1].strip().isdigit() or expresion[i-1].strip().isalpha):
                    esEM=False
                elif i==len(expresion)-1:
                    esEM=False
                else:
                    siguienteValor=True
            elif siguienteValor and not(expresion[i].strip().isdigit() or expresion[i].strip().isalpha()):
                esEM=False
                siguienteValor=False
            elif i<len(expresion)-1 and (expresion[i].strip().isdigit() or expresion[i].strip().isalpha()) and not (expresion[i+1] in ["+","-","*","/","%"]):
                esEM=False
            i+=1
        return esEM
print(esExpresionMatematica("5 + 6 / 7 - 4"))
print(esExpresionMatematica("5 + 6 / a - 4"))
print(esExpresionMatematica("5 + 6 / 7 - 4 +"))
print(esExpresionMatematica("5 + 6 / 7 - 4 5"))
print(esExpresionMatematica("5 a 6"))

                