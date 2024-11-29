#/*
 #* Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 #* - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 #* - EXTRA: ¿Eres capaz de dibujar más figuras?
 #*/


def triangulo(base):
    pintar=""
    cont=0
    puntoAlante=-1
    puntoAtras=-1
    while cont<base//2:
        annadido=False
        for j in range(base):
            if base//2==j and cont==0:
                puntoAlante=base//2+1
                puntoAtras=base//2-1
                pintar+="* "
            elif puntoAlante==j and not annadido and cont!=0:
                annadido=True
                puntoAlante+=1
                pintar+="* "
            elif puntoAtras==j and cont!=0:
                puntoAtras-=1
                pintar+="* "
            else:
                pintar+="  "
        pintar+="\n"
        cont+=1
    for i in range(base):
        pintar+="* "
    print(pintar)

def cuadrado(altura, longitud):
    pintar=""
    for i in range(altura):
        for j in range(longitud):
            if i==0 or i==altura-1:
                pintar+="* "
            elif j==0 or j==longitud-1:
                pintar+="* "
            else:
                
                pintar+="  "
        pintar+="\n"
    print(pintar)

def trapecio(partSuperior, partInferior):
    pintar=""
    diferencia=partInferior-partSuperior
    cont=diferencia
    for i in range(diferencia):
        for j in range (partInferior):
            if i==0 and j>=diferencia-1 and partInferior-diferencia>=j:
                pintar+="* " 
            elif i!=0 and (j==cont-1 or j==partInferior-cont-1):   
                pintar+="* "
            else:
                pintar+="  "
        cont-=1
        pintar+="\n"
    for i in range (partInferior):
        pintar+="* "

    print(pintar)
cuadrado(6,6)
triangulo(7)

trapecio(3,5)

            