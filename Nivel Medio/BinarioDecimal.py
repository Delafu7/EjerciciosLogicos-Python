#/*
 #* Crea un programa se encargue de transformar un número binario
 #* a decimal sin utilizar funciones propias del lenguaje que
 #* lo hagan directamente.
 #
 # /
def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    while binario>0:
        digito=binario%10
        binario = binario//10
        decimal = decimal+ digito*(2**potencia)
        potencia+=1
    return decimal
print(binario_a_decimal(111))