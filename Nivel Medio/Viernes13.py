"""/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
 """
from datetime import date
from convertdate import julian

def hayViernes13(mes, anno):
    # Si el año es menor a 1582, usamos el calendario juliano
    if anno < 1582:
        # Convertimos la fecha juliana (anno, mes, día 13) al calendario gregoriano
        gregorian_date = julian.to_gregorian(anno, mes, 13)
        # Verificamos si el día 13 en el calendario gregoriano es viernes
        fecha = date(gregorian_date[0], gregorian_date[1], gregorian_date[2])
    else:
        # Si el año es posterior a 1582, usamos el calendario gregoriano
        fecha = date(anno, mes, 13)

    # Verificamos si el día de la semana es viernes (weekday() == 4)
    return fecha.weekday() == 4

# Prueba de fechas en ambos calendarios
print(hayViernes13(10, 1307))  # Ejemplo en el calendario juliano
print(hayViernes13(1, 2006)) 
print(hayViernes13(1,2012))
print(hayViernes13(12,1939))
print(hayViernes13(10,1972))
print(hayViernes13(11,2015))
print(hayViernes13(11, 1992))  
print(hayViernes13(12, 2024))  # Ejemplo en el calendario gregoriano
