class Pila:
	"""Representa una pila con operaciones de apilar, desapilar y
	verificar si está vacía."""

	def __init__(self):
		"""Crea una pila vacía."""
		self.items = []

	def apilar(self, x):
		"""Apila el elemento x."""
		self.items.append(x)
	def desapilar(self):
		"""Desapila el elemento x y lo devuelve.
		Si la pila está vacía levanta una excepción."""
		if self.esta_vacia():
			raise ValueError("La pila está vacía")
		return self.items.pop()
	def esta_vacia(self):
		"""Devuelve True si la lista está vacía, False si no."""
		return len(self.items) == 0

class Cola:
	"""Representa a una cola, con operaciones de encolar y
	desencolar. El primero en ser encolado es también el primero
	en ser desencolado."""
	def __init__(self):
		"""Crea una cola vacía."""
		self.items = []
	def encolar(self, x):
		"""Agrega el elemento x como último de la cola."""
		self.items.append(x)
	def desencolar(self):
		"""Desencola el primer elemento y devuelve su
		valor. Si la cola está vacía, levanta ValueError."""
		if self.esta_vacia():
			raise ValueError("La cola está vacía")
		return self.items.pop(0)
	def esta_vacia(self):
		"""Devuelve True si la cola esta vacía, False si no."""
		return len(self.items) == 0
class PilaConMaximo:
	def __init__(self):
		"""Crea una pila vacía."""
		self.items = []
		self.maximos = []

	def apilar(self, x):
		"""Apila el elemento x."""
		self.items.append(x)
		if len(self.maximos) == 0:
			self.maximos.append(x)
		anterior_max = self.maximos.pop()
		if x > anterior_max:
			self.maximos.append(anterior_max)
			self.maximos.append(x)
		else:
			self.maximos.append(anterior_max)

	def desapilar(self):
		"""Desapila el elemento x y lo devuelve.
		Si la pila está vacía levanta una excepción."""
		if self.esta_vacia():
			raise ValueError("La pila está vacía")
		sacado = self.items.pop()
		ultimo_max = self.maximos.pop()
		if sacado != ultimo_max:
			self.maximos.append(ultimo_max)
	def esta_vacia(self):
		"""Devuelve True si la lista está vacía, False si no."""
		return len(self.items) == 0
	def obtener_maximo(self):
		mayor = self.maximos.pop()
		self.maximos.append(mayor)
		return mayor
p = PilaConMaximo()
p.apilar(3)
p.apilar(432)
p.apilar(89)
p.apilar(-123)
p.apilar(43242)
print(p.obtener_maximo())		
