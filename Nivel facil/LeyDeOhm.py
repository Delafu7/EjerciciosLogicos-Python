"""/*
 * Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
 */"""


def leyOhm(V,R,I):
    if V==None and (isinstance(R,float) or isinstance(R,int)) and (isinstance(I,float) or isinstance(I,int)):
        return round(R*I,2)
    elif R==None and (isinstance(V,float) or isinstance(V,int)) and (isinstance(I,float) or isinstance(I,int)):
        return round(V/I,2)
    elif I==None and (isinstance(V,float) or isinstance(V,int)) and (isinstance(R,float) or isinstance(R,int)):
        return round(V/R,2)
    else:
        return "Invalid values"
print(leyOhm(None,10.0,5.0)) 
print(leyOhm(10.0,None,5.0))
print(leyOhm(10,10,None))
print(leyOhm(10,10,10)) # Esto debería devolver "Invalid
print(leyOhm(6.6,5,None)) 
print(leyOhm(None,5,None)) # Esto debería devolver "Invalid"