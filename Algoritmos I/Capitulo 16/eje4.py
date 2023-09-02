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
class Carta:
	def __init__(self, palo, valor):
		self.palo = palo
		self.valor = valor
class solitario:
	def __init__(self):
		self.pila = Pila()
	def apilar_carta(self, carta):
		if self.pila.esta_vacia():
			self.pila.apilar(carta)
		tope = self.pila.desapilar()

		if carta.valor == tope.valor - 1 and carta.palo != tope.palo:
			self.pila.apilar(tope)
			self.pila.apilar(carta)
		

	
s = solitario()
c1 = Carta("espada", 4)
c2 = Carta("basto", 7)
c3 = Carta("copa", 3)
s.apilar_carta(c3)
s.apilar_carta(c1)

