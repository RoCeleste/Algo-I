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

def tail(archivo, n):
	cola = Cola()
	cont = 0
	with open(archivo, "r") as ar:
		for linea in ar:
			linea = linea.strip()
			if cont >= n:
				cola.desencolar()
				cola.encolar(linea)
				cont += 1
			else:
				cola.encolar(linea)
				cont += 1		
			

	for i in range(n):
		print(cola.desencolar())

tail("texto.txt", 30)					