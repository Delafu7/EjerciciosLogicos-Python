#/*
 #* ¡Han anunciado un nuevo "The Legend of Zelda"!
 #* Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
 #* Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
 #* "The Legend of Zelda" de la historia?
 #* Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
 #* que tú selecciones.
 #* - Debes buscar cada uno de los títulos y su día de lanzamiento 
 #*   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
 #*/

from datetime import datetime
def calcularDiferencia(fecha1, fecha2):
    fec1=datetime.strptime(fecha1,'%d-%m-%Y')
    fec2=datetime.strptime(fecha2,'%d-%m-%Y')
    diferencia=abs(fec1-fec2)
    return diferencia.days//365, diferencia.days%365

def lanzamientoTLOZ():
    titulosZelda=["The Legend of Zelda","Zelda II: The Adventure of Link","The Legend of Zelda: A Link to the Past","The Legend of Zelda: Link's Awakening","The Legend of Zelda: Ocarina of Time","The Legend of Zelda: Majora's Mask","The Legend of Zelda: Oracle of Seasons y Oracle of Ages","The Legend of Zelda: The Wind Waker","The Legend of Zelda: Four Swords","The Legend of Zelda: The Minish Cap","The Legend of Zelda: Twilight Princess","The Legend of Zelda: Phantom Hourglass","The Legend of Zelda: Spirit Tracks","The Legend of Zelda: Ocarina of Time 3D","The Legend of Zelda: Four Swords Anniversary Edition","The Legend of Zelda: Skyward Sword","The Legend of Zelda: Oracle of Ages","The Legend of Zelda: Oracle of Seasons","The Legend of Zelda: The Wind Waker HD","The Legend of Zelda: A Link Between Worlds","The Legend of Zelda: Majora's Mask 3D","The Legend of Zelda: Tri Force Heroes","The Legend of Zelda: Twilight Princess HD","The Legend of Zelda: Skyward Sword Wii ","The Legend of Zelda: Breath of the Wild","Cadence of Hyrule - Crypt of the NecroDancer Featuring The Legend of Zelda","The Legend of Zelda: Link's Awakening","The Legend of Zelda: Skyward Sword HD","The Legend of Zelda: Tears of the Kingdom","The Legend of Zelda: Echoes of Wisdom"]
    lanzamientos=["21-2-1986","14-01-1987","21-11-1991","6-6-1993","21-11-1998","27-4-2000","27-2-2001","13-12-2002","8-5-2004","4-11-2004","8-12-2006","19-10-2007","11-12-2009","17-6-2011","28-9-2011","18-11-2011","30-5-2013","30-5-2013","4-10-2013","22/11/2013","13-2-2015","23-10-2015","4-3-2016","1-9-2016","3-3-2017","13-6-2019","20-9-2019","16-7-2021","12-5-2023","26-09-2024"]
    print("Títulos de The Legend of Zelda:\n")
    for i,tituloAnno in enumerate(zip(titulosZelda,lanzamientos)):
        print(f"{i+1}. {tituloAnno[0]} - {tituloAnno[1]} \n")
    titulo1=input("Selecciona un titulo: \n")
    titulo2=input("Selecciona otro titulo: \n")
    if  not titulo1.isalnum() or not titulo2.isalnum() or not (int(titulo1)<=len(titulosZelda) and int(titulo1)>0) or not (int(titulo2)<=len(titulosZelda) and int(titulo2)>0):
        raise ValueError
    annos,dias= calcularDiferencia(lanzamientos[int(titulo1)-1], lanzamientos[int(titulo2)-1])
    print(f"La diferencia entre el título {lanzamientos[int(titulo1)-1]} y el título {lanzamientos[int(titulo2)-1]} es de {annos} años y {dias} días\n")
lanzamientoTLOZ()

    