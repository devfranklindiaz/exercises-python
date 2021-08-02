primero = input('Ingrese primer numero: ')

try: # prueba cambiar el tipo de variable a integer con int()
    primero = int(primero)
except: # sino puede hacerlo, le asigna otro strng a la variable
    primero = 'chanchito feliz'

segundo = input('Ingrese segundo numero: ')
try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

# hacemos el condicional para la suma o validacion 
if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('Ingresaste mal los datos, prueba solo con numeros')
else:
    print('El resultado de la suma es:', primero + segundo)

print('---------- de otra manera usando la funcion exit()-------------')

primero = input('Ingrese primer numero: ')

try: # prueba cambiar el tipo de variable a integer con int()
    primero = int(primero)
except: # sino puede hacerlo, le asigna otro strng a la variable
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un numero por favor prueba nuevamente')
    exit()

segundo = input('Ingrese segundo numero: ')

try: # prueba cambiar el tipo de variable a integer con int()
    segundo = int(segundo)
except: # sino puede hacerlo, le asigna otro strng a la variable
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un numero por favor prueba nuevamente')
    exit()

print(primero + segundo)