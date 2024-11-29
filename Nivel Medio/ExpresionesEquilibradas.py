#* Crea un programa que comprueba si los parentesis, llaves y corchetes
 #* de una expresion estan equilibrados.
 #* - Equilibrado significa que estos delimitadores se abren y cieran
 #*   en orden y de forma correcta.
 #* - Parentesis, llaves y corchetes son igual de prioritarios.
 #*   No hay uno mas importante que otro.
 #* - Expresion balanceada: { [ a * ( c + d ) ] - 5 }
 #* - Expresion no balanceada: { a * ( c + d ) ] - 5 }
#* - Expresion no balanceada: { a * ( c + d ) -

import unittest
def esBalanceado(sentencia):
    pila = []
    diccionario= {')':'(','}':'{',']':'['}
    cont=0
    estaBalanceado= True
    while cont<len(sentencia) and estaBalanceado:
        caracter=sentencia[cont] 
        if caracter in diccionario.values():
            pila.append(caracter)
        elif caracter in diccionario:
            if len(pila)==0 or diccionario[caracter]!=pila.pop():
                estaBalanceado=False
        cont+=1
    if len(pila)!=0:
        estaBalanceado=False
    print(pila)
    return estaBalanceado


class testEstaBalanceado(unittest.TestCase):
    def test_1(self):
        self.assertTrue(esBalanceado("{ [ a * ( c + d ) ] - 5 }"))
    def test_2(self):
        self.assertFalse(esBalanceado("{ a * ( c + d ) ] - 5 }"))
        self.assertFalse(esBalanceado("{ a * ( c + d ) -"))
unittest.main()