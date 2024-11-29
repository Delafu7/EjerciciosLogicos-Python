#* Escribe una funcion que calcule y retorne el factorial de un numero dado
 #* de forma recursiva.

def factorial(n):
    if isinstance(n,int):
        if n==0:
            return 1
        else:
            return n*factorial(n-1)
            #* Escribe una funcion que calcule y retorne el factorial de un numero dado

print(factorial(4))
print(factorial(1))
print(factorial(0))