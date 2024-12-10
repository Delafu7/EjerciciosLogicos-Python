"""/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 */"""

import requests
from bs4 import BeautifulSoup
import re

def main():
    conexion=requests.get("https://holamundo.day")
    soup=BeautifulSoup(conexion.content,"html.parser")
    lineasHTML=soup.find_all("span", class_="rt-Text rt-r-size-4")
    for lineaHTML in lineasHTML:
        frase=str(lineaHTML).split('<strong class="rt-Strong css-ksqtdq">')[1].split("</strong>")
        if bool(re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$',frase[0].strip())):
            print(f"{frase[0]} | {frase[1].removesuffix("</span>")}")

if __name__=="__main__":
    main()
