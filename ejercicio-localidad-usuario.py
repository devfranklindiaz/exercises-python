#-------------------------------------
# Ejercicio de usuarios y localidades
#-------------------------------------
# comentario de prueba
localidades = {
    "San Fernando": ["Alba Juan"],

    "San Miguel": ["Latex Martin", "Perez Anacleto", "Rodriguez Marcelo"],

    "Don Torcuato": ["Acosta Roberto", "Edreira Juana"],

    "Del Viso": ["Martinez Laura", "Alba Juan"],

    "Pilar": ["Edreira Juana"]
}

def menu():
    print("Que desea hacer?")
    print("1) Consultar")
    print("2) Agregar")
    Pregunta1 = input('Respuesta: ')
    return Pregunta1    

def menu2():
    print("Que deseas agregar? ")
    print("1) Usuario")
    print("2)Localidad")
    Pregunta2 = input('Respuesta: ')
    return Pregunta2

def menu3():
    print("Como desea consultar? ")
    print("1) Usuario")
    print("2) Localidad")
    Pregunta3 = input('Respuesta: ')
    return Pregunta3

def consultation():
    consulta = input('Ingrese la localidad: ')
    for localidad, personas in localidades.items():
        if consulta == localidad:            
            var1 = "\n".join(personas)
            #return localidades[consulta] este return te devuelve el valor de la loc1alidad en lista
            return var1     
        else:
            return "Localidad no encontrada"

def consultation1():
    resultado = ""
    consulta2 = input('Ingrese el usuario: ')            
    for localidad, personas in localidades.items():
        for personas in localidades[localidad]:
            if consulta2 == personas:                
                resultado += localidad + "\n"
                
    if resultado == "":
        return "Usuario no encontrado"
    else:
        return resultado    
            
def adduser():
    questlocation = input('¿En qué localidad deseas agregar el usuario?')
    
    if questlocation in localidades: 
        questuser = input('Apellido y nombre que desea agregar: ')
        for localidad, personas in localidades.items():
            if questlocation == localidad:                  
                temp = localidades[questlocation]
                temp.append(questuser)
                localidades[questlocation] = temp
        return localidades[questlocation]
    else:
        return "Localidad no encontrada"

def addlocation():
    Pregunta6 = input('Que localidad deseas agregar? ')
    localidades[Pregunta6] = []
    return localidades

resp = "s"
while resp == "s":
    p1 = menu()

    if p1 == "1":
        pm = menu3()

        if pm == "1":
            newconsul1 = consultation1()
            print(newconsul1)
        elif pm == "2":
            newconsul = consultation()
            print(newconsul)

    elif p1 == "2":
        p2 = menu2()

        if p2 == "1":
            newdic = adduser()
            print(newdic)
        elif p2 == "2":
            newdic = addlocation()
            print(newdic)

    resp = input("Desea realizar otra operacion?:s/n ")