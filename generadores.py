#Estructuras qeu extraen valores de una función y los almacenan en estructuras iterables.
#en vez de return se utiliza yield que construye el objeto iterable y va generando valor por valor(según haga falta).
#Se consiguen funciones más eficientes

#En esta función se crea la lista con todos los valores de golpe
def hacerdorPares(limite):
	numero=1
	lista=[]

	while numero<limite:
		lista.append(numero*2)
		numero=numero+1

	return lista

print(hacerdorPares(10))

#aquí se va generando valor por valor según se va llamando
def hacerdorParesGenerador(limite):
	numero=1
	#lista=[] Ya no hace falta la lista ya que la va a generar sola el generador

	while numero<limite:

		yield numero*2

		numero=numero+1

#Creas un objeto iterable en el que almacenas lo que va devolviendo el generador

almacenador=hacerdorParesGenerador(10)

print(next(almacenador))

#devuelve el primer valor y se queda la función en estado de suspensión hasta que se llame otra vez y genera el siguiente número

print("suspensión.....")

print(next(almacenador))


#YIELD FROM para simplificar el código en caso de bucles anidados.
print(" ")
print("PRUEBA DEL YIELD FROM")
print(" ")

def devuelve_ciudades(*ciudades): #con el * le dices que va a recibir un número indeterminado de elementos en forma de tupla

	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Granada", "Bilbado", "Loja")#al tener el * puedes poner aquí los que quieras

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))


#SIMPLIFICACIÓN CON EL YIELD FROM QUE TE PUEDES PRESCINDIR DEL FOR ANIDADO

def devuelve_ciudades(*ciudades): #con el * le dices que va a recibir un número indeterminado de elementos en forma de tupla

	for elemento in ciudades:
		#for subElemento in elemento:
		yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Granada", "Bilbado", "Loja")#al tener el * puedes poner aquí los que quieras

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))