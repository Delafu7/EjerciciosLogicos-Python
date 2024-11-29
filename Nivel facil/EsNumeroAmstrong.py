#/*
 #* Escribe una funcion que calcule si un numero dado es un numero de Armstrong
 #* (o tambien llamado narcisista).
 #* Si no conoces que es un numero de Armstrong, debes buscar informacion
 #* al respecto.
 #*/

def esNumeroAmstrong(num):
    contadorNum=0
    numAux=num
    while(numAux!=0):
        contadorNum+=(numAux%10)**3
        numAux//=10
    
    return contadorNum==num

print(esNumeroAmstrong(371)) # True
print(esNumeroAmstrong(123)) # False
print(esNumeroAmstrong(0)) # True
print(esNumeroAmstrong(153))#True