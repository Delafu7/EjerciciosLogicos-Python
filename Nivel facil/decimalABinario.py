# * Crea un programa se encargue de transformar un numero
 #* decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def decimalABinario(decimal):
    if isinstance(decimal,int):
        binario = ""
        aux=decimal
        while aux!=0:
            binario= str(aux%2)+binario
            aux=aux//2
            if aux==1:
                binario="1"+ binario
                aux=0
        return binario
print (decimalABinario(4))
print (decimalABinario(5))
print (decimalABinario(36))
