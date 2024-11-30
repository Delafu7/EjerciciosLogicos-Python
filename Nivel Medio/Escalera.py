"""/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 *"""

def escalera(numEscalones:int):
    if isinstance(numEscalones,int):
        escalones=""
        if numEscalones > 0:
            for j in range((numEscalones+1)*2+1):
                if (numEscalones+1)*2==j:
                    escalones+="_"
                else:
                    escalones+=" "
            for i in range(numEscalones+1):
                for j in range((numEscalones+1)*2):
                    if j == (numEscalones+1)*2 - i*2:
                        escalones+="_|"
                    else:
                        escalones+=" "
                escalones+="\n"
        elif numEscalones < 0:
            numEscalones=-numEscalones
            for j in range((numEscalones+1)*2+1,0, -1):
                if (numEscalones+1)*2+1==j:
                    escalones+="_"
                else:
                    escalones+=" "
            escalones+="\n"
            for i in range(numEscalones+1):
                for j in range((numEscalones+1)*2+1,2,-1):
                    if j == (numEscalones+1)*2 - i*2:
                        escalones+="|_"
                    else:
                        escalones+=" "
                escalones+="\n"
        else:
            escalones="__\n__"
        return escalones
  
print(escalera(-4))
print(escalera(4))
print(escalera(0)) 