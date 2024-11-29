#/*
 #* Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 #* ¿De cuántas maneras eres capaz de hacerlo?
 #* Crea el código para cada una de ellas.
 #*/

print("\nForma1\n")

i=1
while i<=100:
    print(i)
    i+=1

print("\nForma2\n")

for j in range (1,101):
    print(j)

print("\nForma3\n")


i=100

while i>0:
    print(i)
    i-=1

print("\nForma4\n")

for j in range (100,0,-1):
    print(j)

print("\nForma5\n")

rango= list(range(1,101))
for j in rango:
    print(j)

print()

print("\nForma6\n")

my_list=iter(rango)
i=1
while i<=100:
   print(next(my_list))
   i+=1