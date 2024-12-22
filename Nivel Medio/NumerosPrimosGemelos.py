"""/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 *
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */"""

def esPrimo(num:int)->False:
    if num<=1:
        return False
    else:
        for i in range(2, int(num*0.5)+1):
            if num % i ==0:
                return False
        return True
def primosGemelos(num:int)->list:
    lista=[]
    numPrimoAnterior=0
    numPrimoActual=0
    for i in range(3,num+1):
        if esPrimo(i) and numPrimoActual==numPrimoAnterior:
            numPrimoActual=i
        if abs(numPrimoActual-numPrimoAnterior)==2 and esPrimo(i):
            lista.append((numPrimoAnterior,numPrimoActual))
        numPrimoAnterior=numPrimoActual
    return lista

if __name__=="__main__":
    print(primosGemelos(14))


