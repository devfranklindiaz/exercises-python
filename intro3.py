print('------------------ Diccionarios Anidados y otra forma de crearlos ----------------')

# diccionario anidado:
gatitos = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba": {
        "nombre": "Black Mamba",
        "edad": 12
    }
}
print(gatitos)

# diccionarios por separado y por variables:
fluffy = {
    "nombre": "Fluffy Diaz",
    "edad": 4
}
mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

# otra forma para crear diccionarios:

perritos = dict(nombre="Rhaegal", edad=3)
print(perritos)