"""Se puede almacenar de todo con una asociación de tipo "clave : valor" que a cada valor que almacenas en el diccionario
se le asigna una clave única a la hora de crearlo. El orden en el que se almacene da igual"""

diccionario = {"Alemania":"Berlin", "España":"Madrid", "Egipto":"Cairo", 25:"Camela", "surmano":25.4}

#Para acceder al elemento utilizas la clave.

print(diccionario["España"])

#Se puede imprimir entero
print(diccionario)

#Para agregar elementos la clave entre corchetes y el nuevo elemento

diccionario["Italia"] = "Roma"

print(diccionario)

#PAra eliminar se usa del y la clave

del diccionario["España"]

print(diccionario)

#Se pueden utilizar tuplas para las claves de cada uno de los valores

tuplas = ("España", "Francia", "Alemania", "Egipto")

diccionario2 = {tuplas[0]:"Madrid", tuplas[1]:"Paris", tuplas[2]:"Berlin", tuplas[3]:"Cairo"}

print(diccionario2)


#Se pueden almacenar tuplas en un diccionario

diccionario_tuplas = {23:"Pepico", "Paises": tuplas}

print(diccionario_tuplas)

diccionario_tuplas = {23:"Pepico", "Paises": ("España", "Francia", "Alemania", "Egipto")}

print(diccionario_tuplas)

#Se pueden obtener las claves o los valores

print(diccionario.keys())

print(diccionario.values())

print(len(diccionario))

