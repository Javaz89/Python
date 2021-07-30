# condicional if: condiciona una ejecucion con determinada condicion o evaluacion
# comparadores: <, >, ==, !=, <=, >=,
if 2 > 5:
    print("primera")
elif 3 > 5:  # si la primera condicion ya fue verdadera elif no se evalua
    print("segunda")
elif 4 > 5:
    print("tercera")
else:  # si ninguna de todas las condiciones fue verdadera se ejecuta else
    print("cuarta")

# if ternario if y else en una sola linea
print('if verdadero') if 5 > 2 else print('else')

# operadores logicos and, or
if 3 > 2 and 1 > 0:
    print("verdad")
