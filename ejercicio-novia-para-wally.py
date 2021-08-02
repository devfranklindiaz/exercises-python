#from ejemplo_facebook import Personas

# Lista con un solo elemento que contiene varios diccionario
posibles_citas = [{"nombre": "Julia", "sexo": "femenino", "edad": 29,
                    "hobbies": ["correr", "musica", "leer"], "ciudad": "Cordoba"},
                    {"nombre": "Camila", "sexo": "femenino", "edad": 18,
                    "hobbies": ["escribir", "arte"], "ciudad": "Mendoza"},
                    {"nombre": "Lucia", "sexo": "femenino", "edad": 35,
                    "hobbies": ["arte"], "ciudad": "Mendoza"},
                    {"nombre": "Daniel", "sexo": "masculino", "edad": 50,
                    "hobbies": ["boxeo", "arte", "leer"], "ciudad": "Mendoza"},
                    {"nombre": "Pepe", "sexo": "masculino", "edad": 32,
                    "hobbies": ["correr", "leer"], "ciudad": "Cordoba"},
                    {"nombre": "Juan", "sexo": "masculino", "edad": 41,
                    "hobbies": ["alpinismo", "juegos de mesa", "leer"], "ciudad": "Cordoba"}]


resul = "" # Variable para almacenar el nombre en string de o las personas que coinciden con los filtros de Wally
temp = [] # Se Almacena los nombres como listas para despues formatearlas a string con la variable resul

for personas in posibles_citas: # for que recorre la lista posible_citas
    for clave, valor in personas.items(): # dentro de la lista posible_citas tenemos varios diccionarios los cuales recorremos
        if type(personas[clave]) == str or type(personas[clave]) == list: # filtra lo que no sea int() para empezar con la primera busqueda
            pass
        else:
            if personas[clave] >= 30: # filtra por edad
                for clave, valor in personas.items(): # recorre los diccionarios resultantes del filtro edad >= 30
                    if personas[clave] == "Mendoza": # filtro por ciudad
                        for clave, valor in personas.items(): # recorre los diccionarios resultantes del filtro ciudad = Mendoza
                            if personas[clave] == "femenino": # filtro por sexo, Wally busca Novia
                                for clave, valor in personas.items(): # recorre los diccionarios resultantes del filtro sexo = femenino
                                    if type(personas[clave]) == list: # Filtro si el valor de la clave hobbies es una lista
                                        for hobbies in personas[clave]: # recorro la lista 
                                            if hobbies == "arte": # filtro por hobbies = arte
                                                temp.append(personas["nombre"]) # almacena en temp los nombres resultantes del filtro arte
                                                resul = ", ".join(temp) # Convierte a string 
print(resul)