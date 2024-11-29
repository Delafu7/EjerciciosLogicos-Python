#/*
 #* Crea un función, que dado un año, indique el elemento 
 #* y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 #* - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 #* - El ciclo sexagenario se corresponde con la combinación de los elementos
 #*   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
 #*   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
 #*   (en este orden).
 #* - Cada elemento se repite dos años seguidos.
 #* - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
 #*/

def crearZodiaco():
    elementos = ["madera", "fuego", "tierra", "metal", "agua"]
    animales = ["rata", "buey", "tigre", "conejo","dragón", "serpiente", "caballo","oveja","mono","gallo","perro","cerdo"]
    zodiaco = {}
    cont=0
    i=0
    j=0
    for anno in range(1924,1984):
        if j==len(animales):
            j=0
        if i==len(elementos):
            i=0
        if cont<2:
            cont+=1
            zodiaco[anno]=[elementos[i],animales[j]]
        if cont==2:
            cont=0
            i+=1
        j+=1
    return zodiaco

def sexagenarioChino(anno):
    zodiaco=crearZodiaco()
    enc=False
    lista=list(zodiaco.keys())
    i=0
    if anno in lista:
        return zodiaco[anno]
    while i<len(lista) and not enc:
        if abs(lista[i]-anno)%60==0:
            enc=True
        else:
            i+=1
    return zodiaco[lista[i]]

print(sexagenarioChino(2073))
print(sexagenarioChino(1953))
print(sexagenarioChino(1893))
print(sexagenarioChino(1976))
print(sexagenarioChino(2003))
print(sexagenarioChino(1972))
print(sexagenarioChino(1979))
print(sexagenarioChino(2018))
print(sexagenarioChino(2020))
print(sexagenarioChino(1981))
print(sexagenarioChino(1975))
    

