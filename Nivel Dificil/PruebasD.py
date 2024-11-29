import  unittest
from TresEnRaya import ganadorTresEnRaya

class ganadorTR(unittest.TestCase):
    def test_ganador_X(self):
        self.assertEqual(ganadorTresEnRaya([["","X","O"],[" ","X","O"],[" ","X",""]]),"X")
        self.assertEqual(ganadorTresEnRaya([["X","O","O"],["X","X","O"],["O","O","X"]]),"X")
    def test_ganador_O(self):
        self.assertEqual(ganadorTresEnRaya([["X","O","O"],["X","O","X"],["O","O","X"]]),"O")
        self.assertEqual(ganadorTresEnRaya([["X","X","O"],["X","O","X"],["O","O","X"]]),"O")
    def test_empate(self):
        self.assertEqual(ganadorTresEnRaya([["X","X","O"],["O","O","X"],["X","X","O"]]),"Nulo")

unittest.main()
