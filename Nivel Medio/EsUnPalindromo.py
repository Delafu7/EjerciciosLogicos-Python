#* Escribe una funcion que reciba un texto y retorne verdadero o
 #* falso (Boolean) segun sean o no palindromos.
 #* Un Palindromo es una palabra o expresion que es igual si se lee
 # * de izquierda a derecha que de derecha a izquierda.
 #* NO se tienen en cuenta los espacios, signos de puntuacion y tildes.
 #* Ejemplo: Ana lleva al oso la avellana.

def esPalindromo(string):
    if isinstance(string, str):
        texto=string.replace(" ", "").lower()
        texto = ''.join(e for e in texto if e.isalnum())
        textoInverso=""
        textoInverso+=texto[::-1]
        return textoInverso==texto
print(esPalindromo("Ana lleva al oso la avellana."))


def esPalindromo1(string):
    if isinstance(string, str):
        texto=string.replace(" ", "").lower()
        texto = ''.join(e for e in texto if e.isalnum())
        textoInverso=""
        for letra in texto:
            textoInverso=letra+textoInverso
        print(textoInverso)
        return textoInverso==texto
print(esPalindromo1("Ana lleva al oso la avellana."))