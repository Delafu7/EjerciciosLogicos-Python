"""/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */"""

#x  se comvierte de x en un número hexadecimal y de dos digitos 02x
def RGB_a_HEX(r,g,b):
    return f"#{r:02x}{g:02x}{b:02x}".upper()

#int(hex[i:i+2], 16) convierte cada par de caracteres hexadecimales en su valor decimal usando la base 16
def HEX_a_RGB(hex):
    return tuple(int(hex[i:i+2], 16) for i in (1, 3, 5))
print(HEX_a_RGB("#000000"))

print(RGB_a_HEX(255, 0, 0))  # Salida: #FF0000 (rojo)
print(RGB_a_HEX(0, 255, 0))  # Salida: #00FF00 (verde)
print(RGB_a_HEX(0, 0, 255))  # Salida: #0000FF (azul)
print(RGB_a_HEX(255, 255, 255))  # Salida: #FFFFFF (blanco)
print(RGB_a_HEX(0, 0, 0))  # Salida: #000000 (negro)

print(HEX_a_RGB("#FFFFFF"))  # Salida: (255, 255, 255)
print(HEX_a_RGB("#FF0000"))  # Salida: (255, 0, 0)
print(HEX_a_RGB("#00FF00"))  # Salida: (0, 255, 0)
print(HEX_a_RGB("#0000FF"))  # Salida: (0, 0, 255)
