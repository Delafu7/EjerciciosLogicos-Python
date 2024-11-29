"""/*
 * Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
 * indicándole únicamente el tamaño del lado.
 *
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
 */"""

def pascal(lista,altura):
    if altura==0:
        return []
    if len(lista) == 1:
        lista.append([lista[0][0],lista[0][0]])
        pascal(lista, altura-1)
    else:
        nueva = [lista[0][0]]
        i=0
        j=1
        while j<len(lista[len(lista)-1]):
            nueva.append(lista[len(lista)-1][i]+lista[len(lista)-1][j])
            i+=1
            j+=1
        nueva.append(lista[0][0])
        lista.append(nueva)
        pascal(lista,altura-1)
def trianguloPascal(base,altura):
    lista=[[base]]
    pascal(lista, altura-1)
    pintar=""
    for i in lista:
        pintar+="".join(f" {str(elem)} " for elem in i )+"\n"
    print(pintar)
    return(lista)
lista=trianguloPascal(1,6)
print( lista)