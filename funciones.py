def funcionjavaz():
    print('no funciona XD')

# funcionjavaz()

def imprimirDato(*argumento1):
    print('el dato es: ',argumento1)

# imprimirdato('parametro1','abc','123','javaz')

def nombreCompleto(apellido,nombre):
    print(nombre,apellido)

# nombreCompleto(nombre='javaz',apellido='GT')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

# nombreCompleto2(nombre='javaz',apellido='Gt')

def funcionjavaz2(dato = 'eu'):
    print(dato)

# funcionjavaz2('javaz')

def funcionlista(lista):
    for x in lista:
        print(x)

# funcionlista(['abc','123'])

def funcionConcatNames(lista):
    i=''
    for x in lista:
        i=i+x+' '
    return i

datos = funcionConcatNames(['abc','123'])

# print(datos)
#recursividad puede usarse en situaciones como el calculo de ciertos metodos numericos que reconocen un caso base para culminar las iteraciones, debe utilizarse solo cuando sea necesario y no exista otra manera....
def recursion(i):
    if (i<1):
        return i
    print(i)
    recursion(i - 1)

recursion(10)