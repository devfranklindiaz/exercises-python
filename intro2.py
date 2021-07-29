print('----------metodo reverse y sort-------------------')


lista = ['hola', 2, 3, 4, 'mundo']

print(lista)

lista.reverse() # muestra los elementos al revés  

print(lista)

#lista.sort() #para ordenar, tienen que tener el mismo tipo de dato
#print(lista)

# tuplas no se puede modificar sus elementos

tupla = ('hola', 'mundo', 'somos', 'tupla')
print(tupla)
#pasar una tupla a lista/arreglo
listadetupla = list(tupla)
listadetupla.append('hola')
print(listadetupla)

# rangos
rango = range(6)
print(rango)

# diccionarios se utilizan para acceder a los valores con nombres de los mismos en vez de con un indice
print('-------------diccionarios -------------------')
diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "persa",
    "edad": 5
}
print(diccionario)
print(diccionario['nombre']) # para mostrar un solo elemento hay que usar []
print(diccionario.get('nombre')) # otro metodo para acceder a un valora solamente
diccionario['nombre'] = 'fluffy' # cambiar el valor de un elemento del diccionario 
print(diccionario)

diccionario['ronronea'] = 'Si' # agregar valores al diccionario y su valor
print(diccionario)
copiaGatito = diccionario.copy() # copiar el diccionario
copiaGatito2 = dict(diccionario) # otra manera de copiar el diccionario 
diccionario.pop('ronronea') # eliminar un valor del diccionario 
print(diccionario)
diccionario.popitem() # eliminar el último valor que se agregó al diccionario
print(diccionario)
del diccionario['raza'] # eliminar valor que le asignes 'otra manera de hacerlo'
print(diccionario, copiaGatito)
#diccionario.clear() # elimina todos los elementos del diccionario 

print('--------------- Diccionarios Anidados ----------------------')



