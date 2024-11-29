#/*
# * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
# * y retorne lo siguiente:
 #* - "X" si han ganado las "X"
 #* - "O" si han ganado los "O"
 #* - "Empate" si ha habido un empate
 #* - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 #*   O si han ganado los 2.
 #* Nota: La matriz puede no estar totalmente cubierta.
 #* Se podría representar con un vacío "", por ejemplo.
 #*/

def ganadorTresEnRaya(resultado):
        gana=False
        ganador="Nulo"
        i=0
        
        while i<len(resultado) and not gana:
                j=0
                while j<len(resultado[0]) and not gana:
                        if resultado[i][j].upper()=="X" or resultado[i][j].upper()=="O":  
                                if j+2<len(resultado[0]) and resultado[i][j]==resultado[i][j+1]==resultado[i][j+2]:
                                        gana=True
                                if i+2 <len(resultado) and resultado[i][j]==resultado[i+1][j]==resultado[i+2][j]:
                                        gana=True
                                if i+2<len(resultado) and j+2<len(resultado[0]) and resultado[i][j]==resultado[i+1][j+1]==resultado[i+2][j+2]:
                                        gana=True
                                if i+2<len(resultado) and j-2>=0 and resultado[i][j]==resultado[i+1][j-1]==resultado[i+2][j-2]:
                                        gana=True
                        j+=1
                i+=1
        if gana:
               ganador=str(resultado[i-1][j-1])
        return ganador