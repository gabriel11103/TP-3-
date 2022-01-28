def validar_entero(msg, limite_inferior, limite_superior):
	x = int(input(msg))
	while x < limite_inferior or x > limite_superior:
		print('El valor debe ser entre', limite_inferior, 'y', limite_superior)
		x = int(input(msg))

	return x


def pedir_titulo():
	titulo = input('Titulo:')
	while len(titulo) == 0:
		titulo = input('Ingrese un titulo correcto:')

	return titulo


def pedir_idioma():
	idioma = int(input('Idioma (1: español, 2: inglés, 3: francés, 4:italiano, 5:otros): '))
	while idioma < 1 or idioma > 5:
		idioma = int(input('Ingrese un idioma correcto:'))

	return idioma - 1


def pedir_precio():
	precio = int(input('Precio: '))
	while precio < 50 or precio > 10000:
		precio = int(input('Ingrese un precio entre 50 y 10.000: '))

	return precio


def pedir_genero():
	genero = int(input(
		'Genero (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía, 5: Escolar, 6: Sociedad, 7: Gastronomía,'
		' 8: Infantil , 9: Otros).: '))
	while genero > 9 or genero < 0:
		genero = int(input('Ingrese el nro del genero correctamente: '))

	return genero


def validar_guiones_isbn(isbn):
	contador_guiones = 0
	guion = False
	guion_correcto = True
	contador_letras = 0
	for car in isbn:
		if car == '-' and guion:
			guion_correcto = False
		elif car == '-' and contador_letras >= 2:
			contador_guiones += 1
		else:
			contador_letras += 1
			guion = False

	if contador_guiones == 3 and guion_correcto:
		return True
	else:
		return False


def validar_numeros_isbn(isbn):
	isbn = isbn.replace('-', '')
	index_codigo = 0
	suma = 0

	for i in range(10, 0, -1):
		suma += int(isbn[index_codigo]) * i
		# print(f'{isbn[index_codigo]} *{i}')
		index_codigo += 1

	# print('Suma: ', suma)
	return True if suma % 11 == 0 else False


def pedir_isbn():
	isbn_valido = False
	isbn = input('Ingrese un isbn: ')

	while not isbn_valido:

		if validar_numeros_isbn(isbn) and validar_guiones_isbn(isbn):
			isbn_valido = True

		else:
			isbn = input('Ingrese un isbn correcto: ')

	return isbn


def prueba():
	isbn = pedir_isbn()
	print(isbn)


if __name__ == '__main__':
	prueba()
