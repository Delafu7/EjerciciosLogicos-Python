#/*
# #* Simula el funcionamiento de una máquina expendedora creando una operación
 #* que reciba dinero (array de monedas) y un número que indique la selección
 #* del producto.
 #* - El programa retornará el nombre del producto y un array con el dinero
 #*   de vuelta (con el menor número de monedas).
 #* - Si el dinero es insuficiente o el número de producto no existe,
 #*   deberá indicarse con un mensaje y retornar todas las monedas.
 #* - Si no hay dinero de vuelta, el array se retornará vacío.
 #* - Para que resulte más simple, trabajaremos en céntimos con monedas
 #*   de 5, 10, 50, 100 y 200.
 #* - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 #*/

productos= {1:5,2:200}


class MonedaNotFound_Error (Exception):
    """Clase para manejar errores de monedas incorrectas"""
class ProductoNoExiste_Error (Exception):
    """Clase para manejar errores de productos no existentes"""
class DineroInsuficiente_Error (Exception):
    """Clase para manejar errores de dinero insuficiente"""

def calcularCambio(diferencia, monedasPermitidas):
    cambio = []
    moneda=0
    while moneda< len(monedasPermitidas):
        if monedasPermitidas[moneda]<=diferencia:
            cantidad = diferencia//monedasPermitidas[moneda]
            diferencia -= monedasPermitidas[moneda]*cantidad
            for i in range(cantidad):
                cambio.append(monedasPermitidas[moneda])
        moneda+=1
    return cambio

def funcionamientoMaqExp(dineroIntro,selecProduc):
    try:
        if isinstance(dineroIntro,list) and all( isinstance(dinero,int) for dinero in dineroIntro) and isinstance(selecProduc,int):
            
            monedasPosibles=[5,10,50,100,200]
            contDineroIntro=0
            for dinero in dineroIntro:
                if dinero in monedasPosibles:
                    contDineroIntro+=dinero
                else:
                    raise MonedaNotFound_Error("La moneda "+str(dinero)+" no es valida.\n")
            if  not selecProduc in productos.keys():
                raise ProductoNoExiste_Error
            if contDineroIntro<productos[selecProduc]:
                raise DineroInsuficiente_Error
            else:
                monedasDeVuelta=[]
                if contDineroIntro>productos[selecProduc]:
                    dif=contDineroIntro-productos[selecProduc]
                    monedasDeVuelta=calcularCambio(dif, sorted(monedasPosibles,reverse=True))
                return monedasDeVuelta
    except MonedaNotFound_Error:
        print("Las monedas que han sido introducidas no son validas\n")
        return dineroIntro
    except ProductoNoExiste_Error:
        print("El producto seleccionado no existe\n")
        return funcionamientoMaqExp(dineroIntro, int(input("Por favor, introduce un número de un producto válido \n")))
    except DineroInsuficiente_Error:
        print("No has introducido suficiente dinero para comprar el producto\n")
        return dineroIntro
    except Exception:
        print("Ha ocurrido un error en la función funcionamientoMaqExp\n")


            
