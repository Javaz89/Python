primero = input('ingrese primer numero: ')
try:
    primero = int(primero)
except:
    print('Debes ingresar un numero... ')
    exit()
segundo = input('ingrese segundo numero: ')
try:
    segundo = int(segundo)
except:
    print('debes ingresar solo numeros...')
    exit()
operador=input('ingrese el operador: ')

if operador == '+':
    print(primero+segundo)
elif operador == '-':
    print(primero-segundo)
elif operador == '*':
    print(primero*segundo)
elif operador == '/':
    print(primero/segundo)
else:
    print('ingrese un operador valido')
