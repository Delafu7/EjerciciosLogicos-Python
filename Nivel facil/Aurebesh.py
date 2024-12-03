"""/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */"""

from PIL import Image


traductorAAurebesh={"a":"Aurek","b":"Besh","c":"Cresh","ch":"Cherek","d":"Dorm","e":"Esk","Æ":"Enth","eo": "Onith","f":"Forn","g":"Grek","h":"Herf","l":"Isk","j":"Jenth","k":"Krill","kh":"Krenth","l":"Leth","m":"Mern","n":"Nern","ng":"Nen","o":"Osk","oo":"Orenth","q":"Qek","r":"Resh","s":"Senth","sh":"Sen","t":"Trill","th":"Thesh","u":"Usk","v":"Vev","w":"Wesk","x":"Xesh","y":"Yirt","z":"Zerek","0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
def concatenar_horizontal(imagenes):
    # Asegurarse de que todas las imágenes tienen la misma altura
    alturas = [img.height for img in imagenes]
    altura_max = max(alturas)
    imagenes = [img.resize((img.width, altura_max)) for img in imagenes]
    
    # Crear una nueva imagen con el ancho total
    ancho_total = sum(img.width for img in imagenes)
    nueva_imagen = Image.new("RGB", (ancho_total, altura_max))
    
    # Pegar imágenes una al lado de la otra
    x_offset = 0
    for img in imagenes:
        nueva_imagen.paste(img, (x_offset, 0))
        x_offset += img.width
    return nueva_imagen
def traducirAAurebesh(text:str)-> str:
    lista=[]
    traducion=""
    for i in text.lower():
        if i in traductorAAurebesh:
            lista.append(Image.open(f"AurebeshImagenes/{traductorAAurebesh[i]}.png"))
            traducion+=traductorAAurebesh[i]+" "
        else:
            traducion+=i
    imagen_horizontal = concatenar_horizontal(lista)
    imagen_horizontal.show()
    return traducion


print(traducirAAurebesh("delafu"))