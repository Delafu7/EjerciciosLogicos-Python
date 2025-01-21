"""/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */"""

def triplesPitagoricos(n:int)->list:
    if isinstance(n,int):
        triples=[]
        for a in range(1,n+1):
            for b in range(a,n+1):
                for c in range(b,n+1):
                    if a**2+b**2==c**2:
                        triples.append((a,b,c))
        return triples
    else:
        return []
print(triplesPitagoricos(10)) # [(3, 4, 5), (6, 8, 10)]
print(triplesPitagoricos(20)) # [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
print(triplesPitagoricos(30)) # [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (15, 20, 25), (18, 24, 30)]