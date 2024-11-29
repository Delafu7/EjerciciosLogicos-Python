from MaquinaExpendedora import funcionamientoMaqExp
import unittest

class PruebasMEx (unittest.TestCase):
    def test_funcionamientoMaqExp(self):
        self.assertEqual(funcionamientoMaqExp([5],1), [])
        self.assertEqual(funcionamientoMaqExp([5,10,50,100,200],2), [100, 50, 10, 5])
        self.assertEqual(funcionamientoMaqExp([2,5,10,100],2),[2,5,10,100])
        self.assertEqual(funcionamientoMaqExp([5,10,100],2),[5,10,100])
        self.assertEqual(funcionamientoMaqExp([],1),[])
        self.assertEqual(funcionamientoMaqExp([5,10,50,100,200],3),[100, 50, 10, 5]) #Si despues se introduce 2
 
unittest.main()