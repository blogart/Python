#Son listas que no se pueden modificar después de su creación.
#No se pueden añadir, eliminar, mover elementos...
#Se pueden extraer porciones pero no se modifica la tupla, se obtiene una tupla nueva.

tupla = ("hola", "adios", "pepperonni", 12, "hola")

print(tupla[1])

#Hay dos métodos para convertir tuplas en listas y al revés

lista = list(tupla)

print(lista)

tupla2 = tuple(lista)

print(tupla2)

#para ver si algo está dentro de la tupla se usa in

print("adios" in tupla)
print("adio" in tupla)


#para averiguar cuantas veces un elemento está dentro de la tupla se usa count

print(tupla.count("hola"))

#para averiguar la longitud de una tupla se usa len

print(len(tupla))

#Se pueden crear tuplas unitarias, con un único elemento, añadiendo una , al final del primer elemento

unitaria = ("pepe",)

#Se puede prescindir de los paréntesis a la hora de declarar. Se denomina como empaquetado de tupla

tupla3 = 2, 3, "Jose"