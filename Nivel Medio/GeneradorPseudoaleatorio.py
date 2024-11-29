"""/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del
 *   lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */"""


"""Si deseas generar números pseudoaleatorios en Python sin usar el módulo random, puedes implementar un generador de números pseudoaleatorios (PRNG) utilizando métodos matemáticos clásicos como el algoritmo de congruencia lineal. Este es un método sencillo y efectivo.

El algoritmo de congruencia lineal sigue esta fórmula:"""



class LinearCongruentialGenerator:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.state = seed  # Semilla inicial
        self.a = a         # Multiplicador
        self.c = c         # Incremento
        self.m = m         # Módulo

    def next(self):
        # Genera el siguiente número pseudoaleatorio
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def rand_range(self, min_val, max_val):
        # Escala el número generado al rango [min_val, max_val]
        return min_val + self.next() % (max_val - min_val + 1)

# Uso
seed = 12345  # Cambia la semilla para obtener una secuencia diferente
prng = LinearCongruentialGenerator(seed)

# Generar números pseudoaleatorios entre 1 y 100
for _ in range(10):
    print(prng.rand_range(1, 100))

"""def generadorPseudoaleatorio100num():
    seed = 1  # Semilla inicial
    for _ in range(0,10):
        seed = (1103515245 * seed + 12345) % 2**31
        print(seed % 101)  # Genera un número entre 0 y 100
generadorPseudoaleatorio100num()"""