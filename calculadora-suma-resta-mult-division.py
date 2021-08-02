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

simbol = input('Ingrese el simbolo de operacion: ')

if simbol == '+':
    print(primero + segundo)
elif simbol == '-':
    print(primero - segundo)
elif simbol == '*':
    print(primero * segundo)
elif simbol == '/':
    print(primero / segundo)
else:
    print('Ingresaste un simbolo incorrecto')