import random
import validaciones

__author__ = 'Montenegro_90329[1k3]_Seeck_89946[1k3]_Ulloque_89972[1k3]'

nombres = ['Cien años de soledad', 'El señor de los anillos', 'Orgullo y prejuicio', 'Turquía Gastronomía', 'Appetites',
		   'Head first: Design patterns', 'Artificial Intelligence: A Modern approach', 'Pragmatic programmer',
		   'Tus zonas erróneas', 'La riqueza de las naciones']

generos = ['Autoayuda', 'Arte', 'Ficción', 'Computación', 'Economía', 'Escolar', 'Sociedad', 'Gastronomía', 'Infantil',
		   'Otros']

idiomas = ['Español', 'Ingles', 'Frances', 'Italiano', 'Otros']

isbns = ['601-121-781-8', '85-608-7388-0', '84-8181-227-7', '601-934-625-0', '849-736-467-8', '840-309-42-64',
		 '840-805-821-5', '842-370-81-95', '84-8104-473-3', '840-309-426-4', '013-595-705-2', '129-240-113-3',
		 '013-449-416-4', '164-473-208-4', '164-473-207-6', '013-475-759-9', '020-163-361-2', '149-204-345-1',
		 '026-253-305-7', '098-478-286-9']

FORMATO_TABLA = "{:^14} {} {:<45} {} {:<12} {} {:<10} {} {:>5}"


class Libro:
	def __init__(self, isbn, titulo, genero, idioma, precio):
		self.isbn = isbn
		self.titulo = titulo
		self.genero = genero
		self.idioma = idioma
		self.precio = precio

	def __str__(self):
		return FORMATO_TABLA.format(self.isbn, '|', self.titulo, '|', generos[self.genero], '|', idiomas[self.idioma],
									'|', self.precio)


def mostrar_menu(opciones):
	for opcion in opciones:
		print(opcion)


def crear_libro():
	print('**Nuevo libro**')
	isbn = validaciones.pedir_isbn()
	titulo = validaciones.pedir_titulo()
	genero = validaciones.pedir_genero()
	idioma = validaciones.pedir_idioma()
	precio = validaciones.pedir_precio()
	return Libro(isbn, titulo, genero, idioma, precio)


def ordenar_libros_titulos(libros):
	n = len(libros)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if libros[i].titulo > libros[j].titulo:
				libros[i], libros[j] = libros[j], libros[i]


def contar_libros_por_genero(libros):
	conteo_libros = [0] * len(generos)

	for libro in libros:
		conteo_libros[libro.genero] += 1

	return conteo_libros


def crear_datos_aleatorios():
	isbn = random.choice(isbns)
	titulo = random.choice(nombres)
	genero = random.randint(0, 9)
	idioma = random.randint(0, 4)
	precio = random.randint(1000, 10000)

	return Libro(isbn, titulo, genero, idioma, precio)


def mostrar_libros(libros):
	print('_' * 30, 'Listado de libros', '_' * 30)
	print(FORMATO_TABLA.format('ISBN', '|', 'Titulo', '|', 'Genero', '|', 'Iidoma', '|', 'Precio'))
	for libro in libros:
		print(libro)


def obtener_indice_mayor_valor(vec):
	mayor = max(vec)

	for i in range(len(vec)):
		if vec[i] == mayor:
			return i


def buscar_mayor_precio(libros, idioma):
	libro_mayor_precio = libros[0]

	for i in range(len(libros)):
		if libros[i].idioma == idioma and i == 0:
			libro_mayor_precio = libros[i]
		elif libros[i].idioma == idioma and libros[i].precio > libro_mayor_precio.precio:
			libro_mayor_precio = libros[i]

	return libro_mayor_precio


def busqueda_por_isbn(libros, isbn_busqueda):
	for i in range(len(libros)):
		if isbn_busqueda == libros[i].isbn:
			return libros[i]
	return


def busqueda_libros_isbn(isbn_buscar, libros):
	encontrados = []
	no_encontrados = []
	for i in range(len(isbn_buscar)):
		listo = False
		for j in range(len(libros)):
			if isbn_buscar[i] == libros[j].isbn:
				listo = True
				encontrados.append(libros[j])
				break

		if not listo:
			no_encontrados.append(isbn_buscar[i])

	return encontrados, no_encontrados


def obtener_libros_por_genero(libros, genero):
	libros_genero = []
	for i in range(len(libros)):
		if libros[i].genero == genero:
			libros_genero.append(libros[i])

	return libros_genero


def ordenar_libros_precios(libros):
	n = len(libros)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if libros[i].precio < libros[j].precio:
				libros[i], libros[j] = libros[j], libros[i]


def sumar_precios(libros):
	suma = 0

	for libro in libros:
		suma += libro.precio

	return suma


def principal():
	opciones = ('1 - Generar y crear',
				'2 - Mostrar libros',
				'3 - Género más popular',
				'4 - Búsqueda del mayor precio',
				'5 - Búsqueda por ISBN',
				'6 - Consulta de un género',
				'7 - Consulta de precio por grupo',
				'8 - SALIR')
	libros = []
	opcion = 0
	cantidad_libros = int(input('Ingrese la cantidad de  libros: '))

	while opcion != 8:
		mostrar_menu(opciones)
		opcion = validaciones.validar_entero('Ingrese su opcion: ', 1, 8)

		if opcion == 1:

			if len(libros) == cantidad_libros:
				print('Ya cargo los libros')
				continue

			for i in range(cantidad_libros):
				mostrar_menu(('1 - Carga automatica', '2 - Carga manual'))

				opcion_carga_libros = validaciones.validar_entero('Ingrese su opcion: ', 1, 2)

				if opcion_carga_libros == 1:
					libro = crear_datos_aleatorios()
					libros.append(libro)
					print('Libro creado correctamente')
				else:
					libro = crear_libro()
					libros.append(libro)
					print('Libro creado correctamente')
		elif len(libros) > 0:
			if opcion == 2:
				ordenar_libros_titulos(libros)
				mostrar_libros(libros)

			elif opcion == 3:
				cantidad_genero = contar_libros_por_genero(libros)
				may = obtener_indice_mayor_valor(cantidad_genero)
				print(f'El genero mas popular es {generos[may]}')

			elif opcion == 4:
				idioma = validaciones.pedir_idioma()
				libro_mas_caro = buscar_mayor_precio(libros, idioma)
				print(f'El libro mas caro en el idioma {idiomas[idioma]} es \n{libro_mas_caro}')

			elif opcion == 5:

				isbn = validaciones.pedir_isbn()
				libro_encontrado = busqueda_por_isbn(libros, isbn)
				if libro_encontrado:
					libro_encontrado.precio *= 1.1
					libro_encontrado.precio = round(libro_encontrado.precio, 0)
					print('Existe el libro')
					print(libro_encontrado)
				else:
					print('No se encontró el libro')

			elif opcion == 6:
				vector_cantidad_genero = contar_libros_por_genero(libros)
				genero_mas_popular = obtener_indice_mayor_valor(vector_cantidad_genero)
				libros_genero_mas_popular = obtener_libros_por_genero(libros, genero_mas_popular)
				ordenar_libros_precios(libros_genero_mas_popular)
				mostrar_libros(libros_genero_mas_popular)

			elif opcion == 7:
				cantidad_libros = int(input('Cuantos libros desea cargar: '))

				isbn_libros = []
				isbns_solicitados = []

				for libro in libros:
					isbn_libros.append(libro.isbn)
				for i in range(cantidad_libros):
					isbns_solicitados.append(validaciones.pedir_isbn())

				libros_encontrados, libros_no_encontrados = busqueda_libros_isbn(isbns_solicitados, libros)
				print('Libros encontrados.')
				mostrar_libros(libros_encontrados)
				precio_total = sumar_precios(libros_encontrados)
				print(f'El precio total es {precio_total}')

				print('Libros no encontrados.')
				for i in range(len(libros_no_encontrados)):
					print(libros_no_encontrados[i])


if __name__ == '__main__':
	principal()
