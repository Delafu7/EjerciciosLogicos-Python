#/*
 #* ¡La Tierra Media está en guerra! En ella lucharán razas leales
 #* a Sauron contra otras bondadosas que no quieren que el mal reine
 #* sobre sus tierras.
 #* Cada raza tiene asociado un "valor" entre 1 y 5:
 #* - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 #*   Númenóreanos (4), Elfos (5)
 #* - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 #*   Huargos (3), Trolls (5)
 #* Crea un programa que calcule el resultado de la batalla entre
 #* los 2 tipos de ejércitos:
 #* - El resultado puede ser que gane el bien, el mal, o exista un empate.
 #*   Dependiendo de la suma del valor del ejército y el número de integrantes.
 #* - Cada ejército puede estar compuesto por un número de integrantes variable
 #*   de cada raza.
 #* - Tienes total libertad para modelar los datos del ejercicio.
 #* Ej: 1 Peloso pierde contra 1 Orco
 #*     2 Pelosos empatan contra 1 Orco
 #*     3 Pelosos ganan a 1 Orco
 #*/

import os
class RazasBondadosas():
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
    def devolverValor(self):
        return self.valor
class Peloso(RazasBondadosas):
    def __init__(self, nombre):
        super().__init__(nombre, 1)
class SureñoBueno(RazasBondadosas):
    def __init__(self, nombre):
        super().__init__(nombre,2)
class Enano(RazasBondadosas):
    def __init__(self, nombre):
        super().__init__(nombre,3)
class Númenóreano(RazasBondadosas):
    def __init__(self, nombre):
        super().__init__(nombre,4)
class Elfo(RazasBondadosas):
    def __init__(self, nombre):
        super().__init__(nombre,5)

class RazasMalvadas():
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
    def devolverValor(self):
        return self.valor
class Orco(RazasMalvadas):
    def __init__(self, nombre):
        super().__init__(nombre, 2)
class SureñoMalo(RazasMalvadas):
    def __init__(self, nombre):
        super().__init__(nombre,2)
class Goblin(RazasMalvadas):
    def __init__(self, nombre):
        super().__init__(nombre,2)
class Huargo(RazasMalvadas):
    def __init__(self, nombre):
        super().__init__(nombre,3)
class Troll(RazasMalvadas):
    def __init__(self, nombre):
        super().__init__(nombre,5)

def resultadoBatalla(linea):
    miembrosBatalla=str(linea).split(",")
    ptoBuenos=0
    ptoMalos=0
    miembrosBatalla=[elem.split("=") for elem in miembrosBatalla]
    for miembro in miembrosBatalla:
        razaPtos=0
        if miembro[0] in ["Peloso","SureñoBueno","Enano","Númenóreano","Elfo"]:
            razaPtos= globals()[miembro[0]](miembro[0]).devolverValor() # con globals busca las clases que tenga ese nombre, por lo que si se modifica el nombre de la cla
            ptoBuenos+=razaPtos*int(miembro[1])
        elif miembro[0] in ["Orco","SureñoMalo","Goblin","Huargo","Troll"]:
            razaPtos= globals()[miembro[0]](miembro[0]).devolverValor()
            ptoMalos+=razaPtos*int(miembro[1])
    if ptoBuenos>ptoMalos:
        return "Los buenos ganaron la batalla\n"
    elif ptoBuenos<ptoMalos:
        return "Los malos ganaron la batalla\n"
    else:
        return "La batalla terminó en empate\n"
#print(resultadoBatalla("Peloso=1,Orco=1"))
#print(resultadoBatalla("Peloso=2,Orco=1"))
#print(resultadoBatalla("Peloso=3,Orco=1"))

def lectorBatallas():
    archivo = open("batallas.txt", "+r")
    contenido = archivo.readlines()
    contBuenos=0
    contMalos=0
    cont=0
    enc=False
    for i in contenido:
        if not "Los buenos ganaron" in i and not i.isspace() :
            result=resultadoBatalla(i)
            print(result)
            if "buenos" in result:
                contBuenos+=1
            elif "malos" in result:
                contMalos+=1
            cont+=1
        else:
            enc=True
    if not enc:   
        archivo.write(f"\nLos buenos ganaron {contBuenos}, mientras que los malos ganaron {contMalos}")
    elif not "Los buenos ganaron "+str(contBuenos)+", mientras que los malos ganaron "+str(contMalos) in contenido[len(contenido)-1]  :
        contenido[len(contenido)-1]=f"\nLos buenos ganaron {contBuenos}, mientras que los malos ganaron {contMalos}"
        archivo.close()
        with open("batallas.txt","+w") as fich:
            fich.writelines(contenido)
    archivo.close()
lectorBatallas()