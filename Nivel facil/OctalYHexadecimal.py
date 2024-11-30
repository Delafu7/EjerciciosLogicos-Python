"""/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */"""

def decimalAOctal(decimal:int):
    octal=""
    while int(decimal)>0:
        octal=str(int((decimal/8-decimal//8)*8)) + octal
        decimal/=8 
    return int(octal)
print(decimalAOctal(272))
        
def decimalAHexadecimal(decimal:int):
    hexadecimal=""
    convertidor={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while int(decimal)>0:
        hexadecimal=str(convertidor.get(int((decimal/16-decimal//16)*16),int((decimal/16-decimal//16)*16))) + hexadecimal
        decimal/=16
    return str(hexadecimal)
print(decimalAHexadecimal(27813))
print(decimalAHexadecimal(239))    

