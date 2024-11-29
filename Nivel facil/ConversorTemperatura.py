"""/*
 * Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 */"""

import re

class TemperaturaIncorrecta(Exception):
    """La temperatura ha sido introducida de forma incorrecta por el usuario"""
def convertidorTemp(texto):
    try:
        if isinstance(texto,str):
            if re.match( r"[0-9]+°C",texto.upper()):
                return round(float(texto[:-2])*9/5 +32, 2)
            elif re.match( r"[0-9]+°F",texto.upper()):
                return round((float(texto[:-2])-32)*5/9,2)
            else:
                raise TemperaturaIncorrecta("La temperatura ha sido introducida de forma incorrecta")
    except TemperaturaIncorrecta:
        print("La temperatura ha sido introducida de forma incorrecta\n")

print(f"Temperatura de °C a °F: {str(convertidorTemp("23°c"))}")
print(f"Temperatura de °C a °F: {str(convertidorTemp("0°C"))}\n")

print(f"Temperatura de °F a °C: {str(convertidorTemp("23°f"))}")
print(f"Temperatura de °F a °C: {str(convertidorTemp("0°F"))}\n")

convertidorTemp("23°P")
convertidorTemp("23")



