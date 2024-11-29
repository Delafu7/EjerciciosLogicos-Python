from QuickSort import quicksort
from QuickSortAutentico import quicksortOriginal

import unittest

class QSMIO(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort( [5, 1, 2, 1, 1, 3, 5, 1, 5, 1, 99, 231, 234, 12, 121,312, 123, 123, 12, 312, 321, 312, 31, 23, 12, 3123, 123]), [1, 1, 1, 1, 1, 2, 3, 5, 5, 5, 12, 12, 12, 23, 31, 99, 121, 123, 123, 123, 231, 234, 312, 312, 312, 321, 3123])

class QSOriginal(unittest.TestCase):
    def test_quicksort(self):
        arreglo = [5, 1, 2, 1, 1, 3, 5, 1, 5, 1, 99, 231, 234, 12, 121, 312, 123, 123, 12, 312, 321, 312, 31, 23, 12, 3123, 123]
        quicksortOriginal( arreglo,0, len(arreglo)- 1)
        self.assertEqual(arreglo, [1, 1, 1, 1, 1, 2, 3, 5, 5, 5, 12, 12, 12, 23, 31, 99, 121, 123, 123, 123, 231, 234, 312, 312, 312, 321, 3123])

unittest.main()