#Definición de funciones

def mensajes():
	print("Menuda función loco")
	print("no veas")

#Llamada a la función
mensajes()


def suma(a,b):
	print(a+b)


numero1 = 3
numero2 = 5

suma(numero1, numero2)


def suma_return(a,b):
	resultado = a+b
	return resultado



print(suma_return(numero2,numero1))