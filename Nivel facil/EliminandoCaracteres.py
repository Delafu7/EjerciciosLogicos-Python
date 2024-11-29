#Crea una funcion que reciba dos cadenas como parametro (str1, str2)
 #* e imprima otras dos cadenas como salida (out1, out2).
 #* - out1 contendra todos los caracteres presentes en la str1 pero NO
 #*   esten presentes en str2.
 #* - out2 contendra todos los caracteres presentes en la str2 pero NO
 #*   esten presentes en str1.

import unittest
def eliminandoCaracteres(string1, string2):
    subString1=str(string1).lower()
    subString2=str(string2).lower()
    out1=""
    out2=""
    for letra in subString1:
        if letra not in subString2:
            out1+=letra
    for letra in subString2:
        if letra not in subString1:
            out2+=letra
    return out1, out2
    #yield out1
    #yield out2
eliminandoCaracteres("Eneko", "Ene")

class eliminandoCaracteresTest(unittest.TestCase):
    def testEliminandoCaracteres1(self):
        self.assertEqual(eliminandoCaracteres("Eneko", "Ene")[0], "ko")
        self.assertEqual(eliminandoCaracteres("Eneko", "Ene")[1], "")

    def testEliminandoCaracteres2(self):
        self.assertEqual(eliminandoCaracteres( "Ene","Eneko")[0],"" )
        self.assertEqual(eliminandoCaracteres("Ene","Eneko" )[1],"ko")

    def testEliminandoCaracteres3(self):
        self.assertEqual(eliminandoCaracteres("Juan", "Unai")[0],"j")
        self.assertEqual(eliminandoCaracteres("Juan", "Unai")[1],"i")
unittest.main()