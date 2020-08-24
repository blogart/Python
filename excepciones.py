#Son errores en tiempo de ejecución.
#Hay que establecer capturas o controles de excepción para que en caso de que ocurra algún error, el programa siga.

#Se crea un bloque try except y se mete dentro la línea que puede fallar 
def divide(num1,num2):

	try:
		return num1/num2

	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operación errónea"

	finally: #Lo que hay dentro del fanally siempre se va a ejecutar pase lo que pase.
		print("Cálculo finalizado")

"""Si el error no coincide con el que hemos includio en except el programa seguirá fallando.
habría que ir añadiendo tantas excepciones conforme se vayan encontrando.
Se puede hacer un except sin nada y se haría una excepción general, pero te deja un poco a ciegas.

#Instrucción Raise sirve para crear excepciones propias