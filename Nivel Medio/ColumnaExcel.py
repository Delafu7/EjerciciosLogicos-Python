""""/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */
 """
import unittest
def ColumnaExcel(nombre:str)->int:
    if isinstance(nombre,str):
        nombre=nombre.upper()
        suma=0
        for i in range(len(nombre)):
            suma+=((ord(nombre[i])-64)*(26**(len(nombre)-i-1)))
        return suma
    else:
        print("Parametro incorrecto")
        raise ValueError
    
class ColumnaExcelTest(unittest.TestCase):
    def test(self):
        self.assertEqual(ColumnaExcel("AA"),27)
        self.assertEqual(ColumnaExcel("CA"),79)
        self.assertEqual(ColumnaExcel("Z"),26)
        self.assertEqual(ColumnaExcel("A"),1)
unittest.main()
