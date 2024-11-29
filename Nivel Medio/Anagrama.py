#/*
 #* Reto #1
 #* ES UN ANAGRAMA?
 #* Fecha publicacion enunciado: 03/01/22
 #* Fecha publicacion resolucion: 10/01/22
 #* Dificultad: MEDIA
 #*
 #* Enunciado: Escribe una funcion que reciba dos palabras (String) y retorne verdadero o falso (Boolean) segun sean o no anagramas.
 #* Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 #* NO hace falta comprobar que ambas palabras existan.
 #* Dos palabras exactamente iguales no son anagrama.
 #*

import unittest
def isAnagrama(word1,word2):
    verifier=False
    if isinstance(word1,str) and isinstance(word2,str)  and  word1!=word2 and len(word1)==len(word2) :
        verifier=True
        i1=0
        auxWord=word2
        while i1<len(word1) and not verifier:
            verifier=False
            i2=0
            while not verifier and i2<len(auxWord):
                if word1[i1]==auxWord[i2]:
                    verifier=True
                    if i2==0:
                        auxWord=auxWord[i2+1:]
                    elif i2==len(auxWord)-1:
                        auxWord=auxWord[:len(i2)-2]
                    else:
                        auxWord=auxWord[:i2-1]+auxWord[i2+1:]
                i2+=1
            i1+=1
    return verifier
#Otra forma seria mediante la ordenacion alfabetica.

def isAnagram(word1,word2):
    verifier=False 
    if isinstance(word1,str) and isinstance(word2,str)  and  word1!=word2 and len(word1)==len(word2) :
        word1Aux=''.join(sorted(word1))
        word2Aux=''.join(sorted(word2))
        if word1Aux==word2Aux:
            verifier=True
    return verifier
#CASOS DE PRUEBA

class Anagrama_test(unittest.TestCase):
    def test_anagrama(self):
        self.assertTrue(isAnagrama("listen","netsil"))
        self.assertTrue(isAnagrama("perefil","fileper"))
        self.assertFalse(isAnagrama("anagrama","anagrama"))
        self.assertFalse(isAnagrama(3,"anagram"))
        self.assertFalse(isAnagrama("anagrama",3))
        self.assertFalse(isAnagrama("dump","inteligent"))
class Anagram_test(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(isAnagram("listen","netsil"))
        self.assertTrue(isAnagram("perefil","fileper"))
        self.assertFalse(isAnagram("anagrama","anagrama"))
        self.assertFalse(isAnagram(3,"anagram"))
        self.assertFalse(isAnagram("anagrama",3))
        self.assertFalse(isAnagram("dump","inteligent"))
unittest.main()
