
"""/*
 * Crea un programa que sea capaz de generar e imprimir todas las
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso
 */"""
def permutaciones(palabra:str)->list:
    if isinstance(palabra,str):
        if len(palabra)==1:
            return [palabra]
        else:
            lista=[palabra[i]+j for i in range(len(palabra)) for j in permutaciones(palabra[:i]+palabra[i+1:])]
            return lista
print(permutaciones("sol"))
