#/*
# * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 #* que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 #* - No se pueden utilizar operaciones del lenguaje que
 #*   lo resuelvan directamente.
 #*/

def maxComDiv(num1, num2):
    if isinstance(num1,int) and isinstance(num2,int):
        maxCD=None
        if num1<num2:
            for i in range (1,num1+1):
                if num1%i==0 and num2%i==0:
                    maxCD=i
        else:
            for i in range (1,num1+1):
                if num1%i==0 and num2%i==0:
                    maxCD=i
        return maxCD

def minComMult(num1, num2):
    if isinstance(num1,int) and isinstance(num2,int):
        minCM=1
        divisores=[2,3,5,7]
        div1=[]
        div2=[]
        i=0
        if num1!=0 and num2!=0:
            while (num1>1 or num2>1) and i<len(divisores):
                if num1%divisores[i]==0:
                    num1/=divisores[i]
                    if len(div1)<i+1:
                        div1.append(divisores[i])
                    else:
                        div1[i]*=divisores[i]
                elif num2%divisores[i]==0:
                    num2/=divisores[i]
                    if len(div2)<i+1:
                        div2.append(divisores[i])
                    else:
                        div2[i]*=divisores[i]
                else:
                    if len(div1)>i and i>=len(div2):
                        minCM *=div1[i]   
                    elif  len(div2)>i and i>=len(div1):
                        minCM *=div2[i]
                    elif div1[i]>div2[i]:
                        minCM *=div1[i]
                    else:
                        minCM *=div2[i]
                    i+=1
            
            while len(div1)>i or len(div2)>i:
                if len(div1)>i and i>=len(div2):
                    minCM *=div1[i]   
                elif  len(div2)>i and i>=len(div1):
                    minCM *=div2[i]
                elif div1[i]>div2[i]:
                    minCM *=div1[i]
                else:
                    minCM *=div2[i]
                i+=1   
        return minCM
    

print (maxComDiv(15,20))

print (minComMult(12,8))

print (minComMult(2,12))