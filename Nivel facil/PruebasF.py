import unittest
from Conjuntos import conjunto
from ConversorTiempo import calcularMiliseconds

class PruebasConversorTiempo(unittest.TestCase):
    def test_conversor_tiempo(self):
        self.assertEqual(calcularMiliseconds(0,0,0,1), 1000)
        self.assertEqual(calcularMiliseconds(2,3,4,5), 183845000)
        self.assertEqual(calcularMiliseconds(0,0,0,0), 0)

class PruebasConjuntos(unittest.TestCase):
    def test_conjuntos(self):
        self.assertEqual(conjunto([1,2,3,4,5],[2,3,4],True),[2,3,4])
        self.assertEqual(conjunto([1,2,3,4,5],[2,3,4],False),[1,5])
        self.assertEqual(conjunto("abc","abcdo",True),["a","b","c"])
        self.assertEqual(conjunto("abc","abcdo",False),['d','o'])
        self.assertEqual(conjunto([16,5],[2,3,4],True),[])
        self.assertIsNone(conjunto([16,5],[2,3,4],2))
        self.assertIsNone(conjunto(2,[2,3,4],True))
        self.assertIsNone(conjunto([2,3,4],2,True))
        self.assertEqual(conjunto("abc",["a","b","c","d","o"],True),["a","b","c"])
        self.assertEqual(conjunto(["a","b","c"],"abcdo",False),['d','o'])
        self.assertEqual(conjunto("abc",[],True),[])
        self.assertEqual(conjunto(["a","b","c"],"",False),["a","b","c"])




       

unittest.main()


