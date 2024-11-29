from CarreraObstaculos import carreraDeObstaculos
from ParandoElTiempo import esperarSuma

import unittest

class comProbarCarreraObstaculos(unittest.TestCase):
    def test_CO_correcto(self):
        self.assertTrue(carreraDeObstaculos(["RUN","JUMP","RUN","JUMP"], "_|_|") )
        self.assertTrue(carreraDeObstaculos(["run","run","run"],"___"))
        self.assertTrue(carreraDeObstaculos(["Jump","Jump","Jump"],"|||"))
    def test_CO_incorrecto(self):
        self.assertFalse(carreraDeObstaculos(["RUN","JUMP","RUN","JUMP"],"__||"))
        self.assertFalse(carreraDeObstaculos(["run","run","run"],"__|"))
        self.assertFalse(carreraDeObstaculos(["Jump","Jump","Jump"],"||_"))
        self.assertFalse(carreraDeObstaculos(["RUN","JUMP","RUN","JUMP"],""))
        self.assertFalse(carreraDeObstaculos([],"__|"))

class meParasElTiempo(unittest.TestCase):
    def test_PET_correcto(self):
        self.assertTrue(esperarSuma(5, 5,0),10)
        self.assertTrue(esperarSuma(10, 10,3),20)
unittest.main()



