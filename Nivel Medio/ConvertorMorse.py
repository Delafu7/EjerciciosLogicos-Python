 #* Crea un programa que sea capaz de transformar texto natural a codigo
 #* morse y viceversa.
 #* - Debe detectar automaticamente de que tipo se trata y realizar
 #*   la conversion.
 #* - En morse se soporta raya "-", punto ".", un espacio " " entre letras
 #*   o simbolos y dos espacios entre palabras "  ".
 #* - El alfabeto morse soportado sera el mostrado en
 #*   https://es.wikipedia.org/wiki/Codigo_morse.



morse_Dic= {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-","l":".-..","m":"--","n":"-.","o":"---", "p":".--.","q":"--.-","r":".-.","s":"...","t":"-", "u":"..-", "v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}

def traductor(sentence):
    if isinstance(sentence,str):
        miniSentence=sentence.lower()
        traduccion=""
        if traduccion[0] in morse_Dic.keys():
                    traduccion+=morse_Dic[letter]
                    miniSentence=miniSentence[1:]
        for letter in miniSentence:
            if letter in morse_Dic.keys():
                traduccion+=" "+morse_Dic[letter]
            elif letter == " ":
                traduccion+=" "
        return (traduccion)

import unittest
class TestTraductor(unittest.TestCase):
    def test_traductor(self):
        self.assertEqual(traductor("soS"),"... --- ...")

print(type(traductor("soS")))
unittest.main()

