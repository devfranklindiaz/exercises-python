

print("Que desea hacer?")
print("1) Consultar")
print("2) Agregar")

Pregunta1 = input('Respuesta: ')
localidades = {
        "San Fernando": ["Alba Juan"],

        "San Miguel": ["Latex Martin", "Perez Anacleto", "Rodriguez Marcelo"],

        "Don Torcuato": ["Acosta Roberto"],

        "Del Viso": ["Martinez Laura"],

        "Pilar": ["Edreira Juana"]
    }

if Pregunta1 == "1":
    consulta = input('Ingrese la localidad: ')
    
    if consulta == "San Fernando":
        print(localidades["San Fernando"])

elif Pregunta1 == "2":
    print("Que deseas agregar? ")
    print("1) Usuario")
    print("2)Localidad")

    Pregunta2 = input('Respuesta: ')
    

    if Pregunta2 == "1":
        Pregunta4 = input('¿En qué localidad deseas agregar el usuario?')
        Pregunta5 = input('Apellido y nombre que desea agregar: ')

        if Pregunta4 == "San Fernando":  
            temp = localidades["San Fernando"]
            temp.append(Pregunta5)
            localidades["San Fernando"] = temp

    elif Pregunta2 == "2":
            Pregunta6 = input('Que localidad deseas agregar? ')
            localidades[Pregunta6] = []


        
        
    print(localidades)
