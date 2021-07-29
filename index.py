# esto es un comentario....
if 3 > 5:
    print('me cago')

# variables

x = 5
y = 'javaz XD'

print(x, y)

email = 'javaz@gmail.com'
print(email)

# el nombre de las variables debe tener sentido dependiendo de lo que guarden
# se puede utilizar guinoes bajos al inicio o al medio de una variable
# se utiliza tambien camelcase ejemplo miVar
# las variables con mayuscula generalmente son para variables MIVAR
# se pueden utilizar numeros pero despues de una letra nunca al inicio
# guiones medios no pueden ser utilizados en nombres de variables, ni espacios en blanco

a, b, c = 'a', 'e', 'i'
# al crear variables de esta forma a cada variable se le asigna el valor que
# segun el orden de valores le corresponde al orden de variables.


print(a, c)
# este print devuelve entonces a , i xq a = a, b = e y c = i....

# para asignar el mismo valor a mas de una variable se hace lo siguiente

val1 = val2 = val3 = 'JavasGt'
print(val1, val2, val3)

# concatenar ....
inicio = 'hola '
final = 'mundo'

print(inicio+final)

# el tipo de dato string str guarda palabras o frases se puede crear con comillas simples o dobles.
palabra = 'hello'

palabra2 = "hello comilla doble"

print(palabra, palabra2)

# numeros enteros o numeros sin decimales integer
entero = 21

# tipo float tiene decimales
decimales = 23.21

# numero complejo j
complejo = 1j

print(entero, decimales, complejo)

# listas son coleciones de datos o datos agrupodos en forma de lista ...

lista = [2, 2, 3]  # lista vacia inicializada con []
# realiza una copia de lista y le asigna a lista2 el valor....
lista2 = lista.copy()
lista.append(4)  # metodo append que agrega un elemento a la lista...
lista.clear()  # clear elimina todo el contenido de la lista

print(lista2)
# cuenta la cantidad de veces que se repite el elemento especificado en la lista
print(lista2.count(2))

# len calcula cual es la cantidad de elementos dentro de la lista...
print(len(lista2))

largolista2 = len(lista2)

print(largolista2)  # es exactamente lo mismo que print(len(lista2))
