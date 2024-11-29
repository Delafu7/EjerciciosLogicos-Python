#/*
# * Crea una función que reciba dos array, un booleano y retorne un array.
 #* - Si el booleano es verdadero buscará y retornará los elementos comunes
 #*   de los dos array.
 #* - Si el booleano es falso buscará y retornará los elementos no comunes
 #*   de los dos array.
 #* - No se pueden utilizar operaciones del lenguaje que
 #*   lo resuelvan directamente.
 #*/
def conjunto(array1,array2, booleano):
    if (isinstance(array1,list) or isinstance(array1,str)) and (isinstance(array2,list) or isinstance(array2,str)) and isinstance(booleano,bool):
        conjun=[]
        if booleano:
            for i in array1:
                if i in array2:
                    conjun.append(i)
        else:
            for i in array1:
                if not (i in array2):
                    conjun.append(i)
                else:
                    if isinstance (array2,list):
                        array2.remove(i)
            for i in array2:
                if not (i in array1):
                    conjun.append(i)
        return conjun
    