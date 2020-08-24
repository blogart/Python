#Primero que hay que hacer es importar el modulo io que nos permite manejar los archivos externos
from io import open #se está importando solo el método open

#argumentos(nombre del archivo, w de white para abrirlo en modo escritura )
archivo_texto=open("archivo.txt", "w") #se está creando un archivo desde aquí

frase="No veas loco que flama esto del python \nflamón"

archivo_texto.write(frase)#manipulación del archivo 
archivo_texto.close() #una vez de manipula hay que cerrar el archivo abierto en memoria desde python


archivo_texto=open("archivo.txt", "r")

#para leer la infor que hay en el archivo se puede crear una variable para almacenar lo que se leer

leer=archivo_texto.read()

archivo_texto.close()

print(leer)

archivo_texto=open("archivo.txt", "r")

lineas_texto=archivo_texto.readlines() #conviertes el archivo de texto en una lista manipulable.
#cada línea de texto en un elemento de la lista.

archivo_texto.close()

print(lineas_texto) #te imprime una lista

print(lineas_texto[0])


archivo_texto=open("archivo.txt", "a") #modo append para añadir una nueva línea.

archivo_texto.write("\ncon el append este añades cosas al archivo asi por arte de magia")

archivo_texto.close()

archivo_texto=open("archivo.txt", "r")

print(archivo_texto.read())


#Modificar la posición de un puntero dentro del texto con el método seek(número de caracter donde se situa)
#Desplaza nuevamente el puntero a la posición que le digas en este caso a la 5
archivo_texto.seek(15)

print(" ")

print(archivo_texto.read())#si incluyes en read() un parámetro se detiene en la posición que le digas

archivo_texto.seek(0)

archivo_texto.seek(len(archivo_texto.read())/2)# Devuelve la mitad del texto

print(archivo_texto.read())