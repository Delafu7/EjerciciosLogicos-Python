#/*
# * Crea una función que reciba un texto y muestre cada palabra en una línea,
# * formando un marco rectangular de asteriscos.
 #* - ¿Qué te parece el reto? Se vería así:
 #*   **********
# *   * ¿Qué   *
# *   * te     *
# *   * parece *
# *   * el     *
# *   * reto?  *
# *   **********
# */

def marcoRectangular(mensaje):
    if isinstance(mensaje,str):
        dividirMensaje=mensaje.split()
        contMasLarga=0
        for palabra in dividirMensaje:
            if len(palabra)>contMasLarga:
                contMasLarga=len(palabra)
        contMasLarga+=4
        frase=""
        for j in range (0,contMasLarga):
            frase+="*"
        frase+="\n"
        for palabra in dividirMensaje:
            for j in range (0,contMasLarga):
                if (j==0 or j==contMasLarga-1):
                    frase+="*"
                elif  j!=1 and  (j==2 or len(palabra)+2>j):
                    frase+=palabra[j-2]
                else:
                    frase+=" "
            frase+="\n"
        for j in range (0,contMasLarga):
            frase+="*"
        frase+="\n"
        return frase

print(marcoRectangular("¿Qué te parece el reto?"))
