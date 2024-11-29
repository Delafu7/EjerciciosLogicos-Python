#/*
 #* Crea una funcion que calcule y retorne cuantos dias hay entre dos cadenas
 #* de texto que representen fechas.
 #* - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 # - La funcion recibira dos String y retornará un Int.
 #* - La diferencia en dias sera absoluta (no importa el orden de las fechas).
 #* - Si una de las dos cadenas de texto no representa una fecha correcta se
 #*   lanzara una excepcion.
 #*/

from datetime import datetime
import pdb, traceback, logging
def calcularDia(fecha1, fecha2):
        try:
                date1= datetime.strptime(fecha1, '%d/%m/%Y')
                date2= datetime.strptime(fecha2, '%d/%m/%Y')
                return abs((date2-date1).days)
        except ValueError as ve:
                #traceback.print_exc()
                logging.error(f"Error: {ve}")
                print(''.join(traceback.format_exception(None,ve,ve.__traceback__)))
                print("La fecha ingresada no es correcta")
print(calcularDia("34/09/2024","26/09/2024"))
