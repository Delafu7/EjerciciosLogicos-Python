"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */"""
def estaEnFibonacci(num):
    a, b = 0, 1
    while a < num and b<num:
        a+=b
        b+=a
    return a==num or b==num
def primoFibonacciPar(num):
    texto=f" - Con el número {num} , nos dirá: {num} "

    if num>1 and all( num%numero!=0 for numero in range(2,num)):
        texto+=" es primo"
    else:
        texto+=" no es primo"
    if estaEnFibonacci(num):
        texto+=", es fibonacci"
    else:
        texto+=", no es fibonacci"
    if num%2==0 :  
        texto+=" y es par"
    else:
        texto+=" y es impar"
    return texto
print(primoFibonacciPar(2))
print(primoFibonacciPar(5))
print(primoFibonacciPar(7))
print(primoFibonacciPar(8))