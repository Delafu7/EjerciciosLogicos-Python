"""/*
 * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
 * ciencia y tecnología desde el 1 de diciembre.
 *
 * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
 * lo siguiente:
 * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
 *   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
 * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
 * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
 *
 * Notas:
 * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
 *   y finaliza a las 23:59:59.
 * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
 *   y segundos.
 */"""

from datetime import datetime,timedelta
def calendarioAdviento2024(fecha: datetime):
    # Definimos el calendario de aDEViento 2024
    if datetime(datetime.today().year,12,1)<=fecha and datetime(datetime.today().year,12,24)>=fecha:
       return("🎁")
    else:
        if datetime(datetime.today().year,12,1)>fecha:
            fechaAct=datetime(datetime.today().year,12,1)-fecha
            inicioFrase="Quedan"
        else:
            fechaAct=datetime(fecha-datetime(datetime.today().year,12,24))
            inicioFrase="Ha pasado"
        dias = fechaAct.days
        horas, resto = divmod(fechaAct.seconds, 3600)
        minutos, segundos = divmod(resto, 60)
        return(f"{inicioFrase} {dias} días, {horas:02}:{minutos:02}:{segundos:02}" )
print(calendarioAdviento2024(datetime.now()))

    