from random import randrange
def generarClave(seguridad=8,includ=None,exclud=None):
	'''-------------------------------------------------------
	Esta funcion sirve para crear claves aleatorias una longitud
	de 1 a 25 caracteres, o de 8 si no se especifica.
	-------------------------------------------------------
	seguridad: Establece mediante un entero, la cantidad de caracteres de la clave
	includ: recibe un string con los caracteres extra que el usuario desee incluir
	exclud: recibe un string con los caracteres ue el usuario desee excluir 
	-------------------------------------------------------	
	Ejemplos:
	>>>	generarClave()
	out	DM23*sg8

	>>>	generarClave(seguridad=18, exclud='*/?¿¡!', includ='Ññ')
	out	iIQÑYkñ1uTWhKñ6BvK
	
	>>> generarClave(seguridad=100000, includ='ÇÑñáéíóúÁÉÍÓÚ', exclud='@?¿¡!-_*+=')
	out áÚÓÉCS5eSéúóíXTSDÓÉx2vqWñ4V
	'''
	caracteres=('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_*+@=/¿?¡!')
	if includ!=None:
		for i in (includ):
			if i not in caracteres:
				caracteres+=i
	if exclud!=None:
		for i in exclud:
			caracteres=caracteres.replace(i,'')
	clave=''
	for i in range(seguridad):
		caracter=caracteres[randrange(len(caracteres))]
		clave=clave+caracter
		if i>25:
			break
	return clave
