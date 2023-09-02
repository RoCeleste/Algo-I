class Punto:
	"""Representación de un punto en el plano en
	coordenadas cartesianas (x, y)"""

	def __init__(self, x, y):
		"""Constructor de Punto. x e y deben ser numéricos"""

		self.x = x
		self.y = y
	def distancia(self, otro):
		"""Devuelve la distancia entre ambos puntos."""

		dx = self.x - otro.x
		dy = self.y - otro.y
		return (dx * dx + dy * dy) ** 0.5

	def restar(self, otro):
		"""Devuelve el Punto que resulta de la resta
		entre dos puntos."""

		return Punto(self.x - otro.x, self.y - otro.y)

	def norma(self):
		"""Devuelve la norma del vector que va desde el origen
		hasta el punto. """

		return (self.x * self.x + self.y * self.y) ** 0.5

	def distancia(self, otro):
		"""Devuelve la distancia entre ambos puntos."""

		return self.restar(otro).norma()

	def __str__(self):
		"""Devuelve la representación del Punto como
		cadena de texto."""

		return f"({self.x}, {self.y})"

	def __repr__(self):
		"""Devuelve la representación formal del Punto como
		cadena de texto."""

		return f"Punto({self.x}, {self.y})"

	def __add__(self, otro):
		"""Devuelve la suma de ambos puntos."""

		return Punto(self.x + otro.x, self.y + otro.y)
	def __sub__(self, otro):
		"""Devuelve la resta de ambos puntos."""

		return Punto(self.x - otro.x, self.y - otro.y)

class Rectangulo:	
	"""Representa un rectángulo en el plano"""

	def __init__(self, noroeste, sudeste):
		"""Crea un Rectangulo a partir de los Puntos correspondientes a las
		esquinas superior izquierda e inferior derecha"""

		self.noroeste = noroeste
		self.sudeste = sudeste

	def __str__(self):
		"""Devuelve la representación del Punto como
		cadena de texto."""

		return f"({self.x}, {self.y})"

	def __repr__(self):
		"""Devuelve la representación formal del Punto como
		cadena de texto."""

		return f"Rectangulo({self.x}, {self.y})"

	def ancho(self):
		return self.sudeste.x - self.noroeste.x

	def alto(self):
		return self.sudeste.y - self.noroeste.y

