# esto es un comentario....
if 3 > 5:
    print('me cago')

# variables

x = 5
y = 'javaz XD'

#print(x, y)

email = 'javaz@gmail.com'
# print(email)

# el nombre de las variables debe tener sentido dependiendo de lo que guarden
# se puede utilizar guinoes bajos al inicio o al medio de una variable
# se utiliza tambien camelcase ejemplo miVar
# las variables con mayuscula generalmente son para variables MIVAR
# se pueden utilizar numeros pero despues de una letra nunca al inicio
# guiones medios no pueden ser utilizados en nombres de variables, ni espacios en blanco

a, b, c = 'a', 'e', 'i'
# al crear variables de esta forma a cada variable se le asigna el valor que
# segun el orden de valores le corresponde al orden de variables.


#print(a, c)
# este print devuelve entonces a , i xq a = a, b = e y c = i....

# para asignar el mismo valor a mas de una variable se hace lo siguiente

val1 = val2 = val3 = 'JavasGt'
#print(val1, val2, val3)

# concatenar ....
inicio = 'hola '
final = 'mundo'

# print(inicio+final)

# el tipo de dato string str guarda palabras o frases se puede crear con comillas simples o dobles.
palabra = 'hello'

palabra2 = "hello comilla doble"

#print(palabra, palabra2)

# numeros enteros o numeros sin decimales integer
entero = 21

# tipo float tiene decimales
decimales = 23.21

# numero complejo j
complejo = 1j

#print(entero, decimales, complejo)

# listas son coleciones de datos o datos agrupodos en forma de lista ...

lista = [2, 2, 3, 2, 2, 2, 2]  # lista vacia inicializada con []
# realiza una copia de lista y le asigna a lista2 el valor....
lista2 = lista.copy()
lista.append(4)  # metodo append que agrega un elemento a la lista...
lista.clear()  # clear elimina todo el contenido de la lista

# print(lista2)
# cuenta la cantidad de veces que se ree pite el elemento especificado en la lista
# print(lista2.count(2))

# len calcula cual es la cantidad de elementos dentro de la lista...
# print(len(lista2))

largolista2 = len(lista2)

# print(largolista2)  # es exactamente lo mismo que print(len(lista2))

# imprima el primer elemento de la lista indicada toda lista empieza con el subinice 0
# print(lista2[0])

lista2.pop()  # pop elimina el ultimo elemento de la lista
# remove necesita de un parametro para eliminar el primer elemento encontrado que coincida con este paramentro en la lista.
lista2.remove(2)

# este metodo invierte el orden que tiene actualmente la lista.
lista2.reverse()
lista2.sort()  # este metodo ordena listas solo desl mismo tipo de dato

# una tupla es similar a una lista pero estas no poseen metodos para edicion de la tupla, si se desea editar la tupla previamente debe ser convertida en una lista
tupla = ('aaaa', 'bbbb', 'cccc', 'dddd')
listatupla = list(tupla)  # metodo list combierte a lista un parametro dado...
# el tipo de dato rango crea el rango de 0 al parametro dado...
rango = range(6)

# Diccionario  posee clave y valor "clave":"valor" se escribe coma para seguir ingresando mas elementos al diccionario para acceder a alguno de estos elementos se debe ingresar el nombre de dicionario y entre llaves cololar el valor de la clave diccionario["nombre"] lo que devuelve el valor
diccionario = {
    "nombre": "mishisho",
    "raza": "washquero",
    "edad": "1"
}
# ambas formas devuelven el valor de la clave dada
# print(diccionario['nombre'])
# print(diccionario.get('nombre'))
diccionario['nombre'] = "mishisha"  # para editar el valor de una clave
diccionario['color'] = "negro"  # agregando una nueva clave:valor
# elimina un elemento del diccionario con una clave dada.
copiadic = diccionario.copy()  # hace una copia
# copiadic2 = dict(diccionario)#tambien hace una copia...
diccionario.pop('edad')  # elimina una clave:valor proporcionando la clave
diccionario.popitem()  # elimina la ultima clave:valor agregada...
del diccionario['nombre']  # funciona igual q pop('clave')
diccionario.clear()  # borra todo el diccionario...

# diccionarios anidados son diccionarios dentro de otros diccionarios...

electronicos = {
    "computadoras": {"categoria": "periferico"},
    "hogar": {"categoria": "higiene"}
}

# esta forma tambien permite ingresar clave:valor a un diccionario no es mejor que la vista anteriormente solo es otra forma de hacerlo...

# tipo de dato boolean
bandera = True
bandera2 = False
print(bandera,bandera2)
