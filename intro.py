# asi se hace un comentario 
if 3 > 5:
    print('Esto no se va a imprimir')

if 5 > 3:
    print( '5 es mayor a 3 ')

a = 'chanchito'
b = 5

print(a , b)

y = 'hola '
z = 'mundo'

print(y, z)

inicio, medio, final = 'hola ', 'como ', 'estas?'

print(inicio + medio + final)


inicio1, medio1, final1 = 'hola', 'como', 'estas?'

print(inicio1, medio1, final1)

# tipos de datos

# string
palabra = 'hola'
oracion = "hola como estas?"

# integer (sin decimales)
entero = 20

# float (con decimales)
condecimales = 20.5

# numeros complejos
complejo = 1j

print(palabra, oracion, entero, condecimales, complejo)

# listas
print('---------listas------------')
# para definir lista vacia se inicializa con corchetes
lista = [1, 2, 3]
# para copiar una lista se usa copy()
lista2 = lista.copy()
# para agregar elementos a la lista se usa append
lista.append(4)
# para eliminar todos los elementos de la lista se usa clear
# lista.clear()

print(lista, lista2)


print('----------contar elementos en listas---------------')
# para contar elementos de una lista se usa count
print(lista, lista2.count(2))
# para contar la cantidad de elementos de una lista sin indicar el valora que se repita con la funcion len()
print(len(lista), len(lista2))
# otra forma
largolista = len(lista)
largolista2 = len(lista2)

print(largolista, largolista2)

print('-----------mostrar un elemento en el arreglo/lista-------------------')

print(lista[0])

print('--------------eliminar elementos de un arreglo/lista------------------')
# eliminar con la funcion pop() elimina el ultimo elemento
lista.pop()
print(lista)

# eliminar elementos por su valor con remove()
lista.remove(2)
print(lista)