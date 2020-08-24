#IF
"""
print("Programa de evaluacion de notas de alumnos, introduce la nota del alumno:")

notas = input()

#igual que el cin y en python cualquier cosa que introduzcas es considerado como 
#texto por lo que habría que castear a int para que funciones"""
"""
def evaluacion(nota):
	valoracion = "aprobado"

	if nota < 5:
		valoracion = "suspenso"

	return valoracion

print(evaluacion(int(notas))) #Aqui se castea a int para que el input funcione


#Bucles

#for variable in elemento a recorrer(lista, tupla, cadena texto.....)

for i in [1,2,3]:
	print("buclazo for")


for i in ["primavera", "invierno", "verabno", "otoño"]: #repite tantas veces como elementos tengas.
	print(i, end=" ") #va asignando el valor de cada elemento a i en cada iteración con end imprime sin salto

#Puedes recorrer un string directamente con el bucle puede servir para conprobar direcciones de correo

for i in "quepasalocomenudaflipadaestodelpython":
	print(i, end="")
"""
###########################################################################
"""
print("Mega Programa para comprobar si lo introducido es un correo electrónico")

email=False

correo=input("Introduce la dirección de correo: ")

for i in correo:

	if i=="@":
		email=True
		break; #con eso sale del bucle una vez encuentra el @

if email==True: #if email solamente sería equivalente a email==True
	print("Correo bueno")
else:
	print("Correo malo")
"""
# range() se utiliza para hacer bucles como por ejemplo en c++
"""
for i in range(5):
	print("hola") #imprime hola 5 veces, si le metes el valor de i imprimiría de 0 a 4


for i in range(5):
	print(f"el valor de i es: {i}") # Se utiliza la f para decirle a python que vas a utilizar lo de las llaves


for i in range(11, 19):
	print(f"el valor de i es: {i}")

for i in range(11, 199, 3): #Empieza en el 11 hasta el 198 y va de 3 en 3
	print(f"el valor de i es: {i}")

"""
######################################WHILE#####################################

i=1

while i<=10:
	print("iteración: " + str(i))
	i+=1

print("Fin ejecución")

#se puede utilizar break para salir del bucle cuando uno quiera

"""Intrucciones especiales
-continue salta a la siguiente iteración de bucle ignorando la iteración en la que se añada
-pass devuelve null en cuanto se lee. Es como si no se ejecutara el bucle.
-else igual que en el if
"""
for letra in "Python":

	if letra=="h": #Cuando encuentra la letra h se salta esa iteración y no entra en el print.
		continue

	print(letra)


