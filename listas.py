#Equivalen a los arreglos. puedes guardar dentro el tipo de dato que quieras, y puedes cambiar la dimensión como quieras

lista = ["Polla", "coño", "ojete"]

print(lista[:])
print(lista)#también sirve así

print(lista[1]) #para imprimr un índice concreto.


print(lista[-2]) #si usas número negativo empieza a contar desde el final, pero ya empezando en el número 1



print(lista[1:3]) #imprime los 3 primeros índices, el 0 sería inclusive y el 3 exclusive. Para accesos parciales

#Para agregar elementos se utiliza la función append() y agrega siempre al final

lista.append("berga")

print(lista)

#Para agregar elementos entre medias se utiliza insert(indice, elemento)

lista.insert(0, "pollon")

print(lista)

#Para agregar varios elementos se utiliza extend([elementos a agregar]) los agrega al final

lista.extend(["concha", 6, "big black cock"])

print(lista)

#Para saber en que índice está algun elemento se utiliza index(elemento)

print(lista.index("concha"))

#Para comprobar si un elemento se encuentra o no en una lista se utiliza in te devuelve true o false

print(78 in lista)

#Para eliminar elementos se utiliza remove(elemento)

lista.remove("pollon")

lista.pop() #elimina el último elemento de la lista.

print(lista)


