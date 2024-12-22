"""/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */"""

def construirEspiral(num):
    uzumaki=[]
    for _ in range(num):
        uzumaki.append([""for _ in range(num)])
    inic=0
    final=num
    uzumaki[0][0]="═"
    while inic<final:
        for i in range(inic,final):
           if uzumaki[inic][i]=="":
             uzumaki[inic][i]="═" 
             if i==final-1:
                        uzumaki[inic][i]="╗"
        cont=0        
        for i in range(inic,final):
            if cont==0 and uzumaki[final-1][i]=="" :
                uzumaki[final-1][i]="╚" 
            else:
                if (i==final-1 or uzumaki[final-1][i+1]!=""):
                    if uzumaki[final-1][final-1]=="":
                        uzumaki[final-1][final-1]="╝"
                else:
                    uzumaki[final-1][i]="═" 
            cont+=1
        cont=0
        for i in range (inic+1,final-1):
            if cont==0: 
               uzumaki[inic+1][inic]="╔" 
            else:
                uzumaki[i][inic]="║" 
            cont+=1
        for i in range (inic+1,final-1):
            uzumaki[i][final-1]="║"
        inic+=1
        final-=1
    
    imagen=""
    for i in range(0,num):
        for j in range(0,num):
            imagen+=uzumaki[i][j]
        imagen+="\n"
    print(imagen)
construirEspiral(5)