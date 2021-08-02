dato = input("Ingrese una palabra: ")
print("\n")

lista =["casa", "perro", "gato", "hola", "mundo", 5]

if lista.count(dato) > 0:    
    print("La palabra", dato,  "si existe en nuestra lista :)")
else:
    print("La palbra", dato, "no existe en nuestra lista :(")