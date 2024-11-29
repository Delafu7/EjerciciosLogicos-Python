from PiedraPapelTijera import piedraPapelTijera

import unittest

class PruebaPPT(unittest.TestCase):
    def test_ganador(self):
        self.assertEqual(piedraPapelTijera([("R", "S"),("P","S"),("P","P"),("R","S")]),"Player 1")
        self.assertEqual(piedraPapelTijera([("R","S"), ("S","R"), ("P","S")]),"Player 2")
    def test_empate(self):
        self.assertEqual(piedraPapelTijera([("R", "S"),("P","S"),("P","P")]),"Tie")

unittest.main()