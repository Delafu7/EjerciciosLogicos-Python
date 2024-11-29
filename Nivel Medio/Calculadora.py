
#/*
 #* Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 #* resultado e imprímelo.
 #* - El .txt se corresponde con las entradas de una calculadora.
 #* - Cada línea tendrá un número o una operación representada por un
 #*   símbolo (alternando ambos).
 #* - Soporta números enteros y decimales.
 #* - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 #*   y división "/".
 #* - El resultado se muestra al finalizar la lectura de la última
 #*   línea (si el .txt es correcto).
 #* - Si el formato del .txt no es correcto, se indicará que no se han
 #*   podido resolver las operaciones.
 #*/

import re 

def calcularValor(num2, op, num1):
    result=0
    if op=='+':
        result=float(num1)+float(num2)
    elif op=='-':
        result=float(num1)-float(num2)
    elif op=='*':
        result=float(num1)*float(num2)
    elif op=='/':
        result=float(num1)/float(num2)   
    return str(result)

def calcularResultadoExpr(linea):
    numOP=[]
    lparentesis=[]
    patron=r'[0-9]{1}'
    if isinstance(linea,str):
        sigValor=1
        for carac in linea:
            
            
            if carac in "+-*/" and len(numOP)!=0:
                numOP.append(carac)
            
            elif re.match(patron,carac):
                
                if len(numOP)==0:
                    numOP.append(carac)
                elif  sigValor<len(linea) and (re.match(patron,linea[sigValor]) or re.match(patron,linea[sigValor-1])) :
                    if numOP[len(numOP)-1] in "+-/*" or numOP[len(numOP)-1] in "[(":
                        numOP.append(carac)
                    else:
                        numOP[len(numOP)-1]+=carac
                elif numOP[len(numOP)-1] in "+-" :
                    numOP.append(carac)
                else:
                    numOP.append(carac)

                if sigValor<len(linea) and numOP[len(numOP)-2] in "*/" and not re.match(patron,linea[sigValor]):

                    numOP.append(calcularValor(numOP.pop(),numOP.pop(),numOP.pop()))

            elif carac=='(' or carac=='[':
                lparentesis.append(carac)
                numOP.append(carac)

            elif carac==')' or carac==']' :
                variableEliminada=lparentesis.pop()
                if variableEliminada !='(' and carac==')' :
                    raise ValueError
                elif variableEliminada !='[' and carac==']' :
                    raise ValueError
                else:
        
                    variableEliminada= numOP.pop()
                    numOP.append(variableEliminada)
                    while(len(numOP)>1 and (variableEliminada!='(' and variableEliminada!='[' )):
                        numOP.append(calcularValor(numOP.pop(),numOP.pop(),numOP.pop()))
                        variableEliminada= numOP[len(numOP)-2]
                    if not (variableEliminada!='(' and variableEliminada!='[' ):
                        numOP.pop(len(numOP)-2)
                    if numOP[len(numOP)-2] in "/*":
                        numOP.append(calcularValor(numOP.pop(),numOP.pop(),numOP.pop()))
            sigValor+=1        
        while len(numOP)>1 :
                numOP.append(calcularValor(numOP.pop(),numOP.pop(),numOP.pop()))
        if len(numOP)!=1:
            raise OverflowError
        return numOP.pop()
               
                                            

def calculadoraTXT():
    try:
        fichero= open("fichero.txt","r+")
        contenido = fichero.readlines()
        for linea in contenido:
            print("Operacion: "+linea+" \n Resultado = "+str(calcularResultadoExpr(linea))+"\n")
        fichero.close()
    except OverflowError:
        print("Error de Overflow")
    except ValueError:
        print("Error de sintaxis")
calculadoraTXT()