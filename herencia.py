class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nArrancado: ", self.enmarcha, "\nAcelerando: ", self.acelera, 
			"\nFrenando: ", self.frena)

class Flagoneta(Vehiculos):
	
	def carga(self, cargas):
		self.cargado=cargas
		if(self.cargado):
			print("La Flagoneta está cargada.") #Si aqui pusiese un return a la hora de usar el método hace falta print.
		else:
			print("La Flagoneta no está cargada")

class Moto(Vehiculos): #En los paréntesis pones la clase de la que hereda.
	hcaballito=""
	def caballito(self): #Creas el método para asignarle un valor a la propiedad caballito
		self.hcaballito="Estoy haciendo un caballito"

	#Hay qeu sobreescribir el método estado para que nos muestre también las propiedades de moto
	#Sobreescribe el método estado de la clase padre.
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nArrancado: ", self.enmarcha, "\nAcelerando: ", self.acelera, 
			"\nFrenando: ", self.frena, "\n", self.hcaballito)

class Electricos(Vehiculos):

	def __init__(self, marca, modelo): #En el constructor ya puedes incluir marca y modelo al usar super

		#La función super() llama a los métodos que quieras de la clase padre.
		super().__init__(marca, modelo)

		self.autonomia=200
		
	def carga(self):
		self.cargando=True

	def estado(self):

		super().estado() #También se puede heredar cualquier método y luego añadir tu mas cosas.
		print("Autonomía: ", self.autonomia)

#Herencia múltiple teniendo preferencia la que colocas primero en el ()
class Ebike(Electricos, Vehiculos):
	pass



###########################################################################################################################

Amoto=Moto("Bugatti", "Monster") #Hay que pasarle los parámetros del constructor de la que hereda la clase moto.

Amoto.caballito()

Amoto.estado()

miFurgo=Flagoneta("Renault", "Traffic")

miFurgo.estado()

miFurgo.carga(False)

bici=Ebike("Orbea", "Alma")

bici.estado()

#Para saber si una instancia pertenece a una clase se usa insintance(instancia, clase)
print(isinstance(bici,Vehiculos))