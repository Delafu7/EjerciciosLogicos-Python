#/*
 #* Dado un array de enteros ordenado y sin repetidos,
 #* crea una función que calcule y retorne todos los que faltan entre
 #* el mayor y el menor.
 #* - Lanza un error si el array de entrada no es correcto.
 #*/

import traceback

class ArrayIncorrectoError (Exception):
    """Error surgido cuando no es correcta la array"""

def numPerdidos(conjunto):
    try:
        if not isinstance(conjunto, set) or not all(isinstance(elem,int) for elem in conjunto):
            raise ArrayIncorrectoError("La entrada no es un array")
        else:
            conjunto = sorted(list(conjunto))
            return [i for i in range(conjunto[0], conjunto[-1]+1) if not i in conjunto]
    except ArrayIncorrectoError:
        print("Error: La entrada no es un array")
        traceback.print_exc()
print(numPerdidos({1,2,5,17,9,7,7}))
print(numPerdidos({1,2,5,17,9,7,7}))
print(numPerdidos({1,2,5,17,9,"num",7}))