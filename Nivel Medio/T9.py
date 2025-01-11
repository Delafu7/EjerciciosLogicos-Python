"""/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */"""

def T9(pulsaciones:str)->str:
    try:
        if isinstance(pulsaciones,str):
            pulsaciones=pulsaciones.split("-")
            T9={"2":"ABC","3":"DEF","4":"GHI","5":"JKL","6":"MNO","7":"PQRS","8":"TUV","9":"WXYZ"}
            texto=""
            for pulsacion in pulsaciones:
                if pulsacion[0] in T9 and pulsacion.isdigit() and len(T9[pulsacion[0]])>=len(pulsacion) :

                        texto+=T9[pulsacion[0]][len(pulsacion)-1]
                else:
                    raise ValueError("Pulsación incorrecta")
            return texto
    except ValueError as e:
        return e
    
print(T9("6-666-88-777-33-3-33-888"))
print(T9("6-666-88-777-33-3-33-888-9-99999"))
print(T9("6-666-88-777-33-3-33-888-9-99999-1"))