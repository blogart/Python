#Creación de clases
#Para definir el comportamiento de la clase se definen los métodos.

class Coche():

	#Constructor
	def __init__(self):

		self.largo=250
		self.__ancho=120
		self.__ruedas=4 #Con __ la encapsulas como si fuese private y ya hay que usar __ siempre
		self.__enmarcha=False
		self.__color="rojo"

	#Para crear métodos en la clase se usa defs self es como this y en python hace falta ponerlo siempre en los parámetros.
	#Comportamiento de la clase
	def arrancar(self, arrancado):

		self.__enmarcha=arrancado #el self es como el this

		if(self.__enmarcha==True):
			return "El coche está arrancado"
		else:
			return "El coche está apagado"

	def estado(self):
		print("El coche está flama ", "tiene ", self.__ruedas, "rueda y un largo y ancho tal....")
		

#Instanciación

miCoche=Coche()

print("El largo del coche es: ", miCoche.largo)

miCoche.estado()

print(miCoche.arrancar(True))

miCoche.estado()

miCoche2=Coche()