class Hotel:
	"""Representa un hotel: sus atributos son:
	nombre, ubicacion, puntaje y precio."""
	def __init__(self, nombre, ubicacion, puntaje, precio):
		"""Crea un Hotel.
		nombre y ubicacion deben ser cadenas no vacías,
		puntaje y precio son números."""
		self.nombre = nombre
		self.ubicacion = ubicacion
		self.puntaje = puntaje
		self.precio = precio

	def __str__(self):
		"""Conversión a cadena de texto."""
		return "{} de {} - Puntaje: {} - Precio: {} pesos".format(
		self.nombre,
		self.ubicacion,
		self.puntaje,
		self.precio,
		)

	def ratio(self):
		"""Calcula la relación calidad-precio de un hotel"""
		return ((self.puntaje ** 2) * 10) / self.precio

	def __lt__(self, otro):
		"""Compara dos hoteles según sus ratios."""
		return self.ratio() < otro.ratio()
h1 = Hotel("Hotel 1* normal", "MDQ", 1, 10)
h2 = Hotel("Hotel 2* normal", "MDQ", 2, 40)
h3 = Hotel("Hotel 3* carisimo", "MDQ", 3, 130)
h4 = Hotel("Hotel vale la pena" ,"MDQ", 4, 130)
li = [h1,h2,h3,h4]
li.sort()
for i in li:
	print(i)