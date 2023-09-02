class Nodo:
	def __init__(self, dato=None, prox=None):
		self.dato = dato
		self.prox = prox

	def __str__(self):
		return str(self.dato)
	
	def ver_lista(self):
		"""Recorre todos los nodos a través de sus enlaces,
		mostrando sus contenidos."""

		while self is not None:
			print(self)
			self = self.prox

class ListaEnlazada:
	"""Modela una lista enlazada."""
	def __init__(self):
		"""Crea una lista enlazada vacía."""
		# referencia al primer nodo (None si la lista está vacía)
		self.prim = None
		# cantidad de elementos de la lista
		self.len = 0

	def pop(self, indice):

		if indice > self.len or indice < 0:
			raise Exception("Valor no valido")
		if indice == None:
			indice = self.len - 1
		if indice == 0:
			dato = self.prim.dato
			self.prim = self.prim.prox
		else:
			anterior = self.prim
			actual = anterior.prox
			for pos in range(1, indice):
				anterior = actual
				actual = anterior.prox
			dato = actual.dato
			anterior.prox = actual.prox

		self.len -= 1
		return dato
	def remove(self, valor):
		if self.len == 0:
			raise Exception("No existe ese valor")
		if self.prim.dato == valor:
			self.prim = self.prim.prox
		else:
			anterior = self.prim
			actual = anterior.prox
			while actual is not None and actual.dato != valor:
				anterior = actual
				actual = anterior.prox
			if actual is None:
				raise Exception("Este valor no esta en la lista")
			else:
				anterior.prox = actual.prox	
		self.len -= 1

	def insert(self, pos, valor):
		if pos < 0 or pos > self.len:
			raise Exception("No se puede agregar en esa posicion")
		if pos == 0:
			nuevo = Nodo(valor)
			nuevo.prox = self.prim.prox
			self.prim = nuevo

		else:
			anterior = self.prim
			for i in range(1,pos):
				anterior = actual
				
			nuevo = Nodo(valor)
			nuevo.prox = anterior.prox
			anterior.prox = nuevo
			self.len += 1

	def __str__(self):
		actual = self.prim
		cadena = ""
		for i in range(0, self.len):
			actual = actual.prox
			cadena += f"{actual}, "
		return f"[{cadena[:-2]}]"

	def append(self, valor):
		if self.len == 0:
			nuevo = Nodo(valor)
			self.prim = nuevo
			self.prim.prox = None
		actual = self.prim
		for i in range(0, self.len):
			actual = actual.prox
			
		nuevo = Nodo(valor)
		actual.prox = nuevo
		self.len += 1

	def extend(self, le):
		actual_self = self.prim
		for i in range(0, self.len):
			actual_self = actual_self.prox
		actual_le = le.prim	
		for i in range(0, le.len+1):
			nuevo = Nodo(actual_le.dato)
			actual_self.prox = nuevo
			nuevo.prox = None
			actual_le = actual_le.prox
			actual_self = actual_self.prox
			self.len += 1

	def remover_todos(self, valor):

		if self.prim.dato == valor:
			self.prim = self.prim.prox

		anterior = self.prim
		actual = anterior.prox
		while actual is not None:
			if actual.dato == valor:
				anterior.prox = actual.prox
				
				self.len -= 1
			anterior = actual
			actual = anterior.prox
	def duplicar(self, valor):
		if self.prim.dato == valor:
			nuevo = Nodo(valor)
			nuevo.prox = self.prim.prox
			self.prim.prox = nuevo
		else:
			anterior = self.prim
			actual = anterior.prox
			while actual is not None:
				if actual.dato == valor:
					nuevo = Nodo(valor)
					nuevo.prox = actual
					anterior.prox = nuevo
					self.len += 1
				anterior = actual
				actual = anterior.prox
	def filter(self, funcion):
		le = ListaEnlazada()
		if funcion(self.prim.dato) == True:
			nuevo = Nodo(self.prim.dato)
			le.prim = nuevo
			le.prox = None
		
		anterior_self = self.prim
		actual_self = anterior_self.prox
		anterior_le = le.prim
		while actual_self is not None:
			if funcion(actual_self.dato) == True:
				nuevo = Nodo(actual_self.dato)
				anterior_le.prox = nuevo
				nuevo.prox = None
				anterior_le = nuevo
				le.len += 1
			anterior_self = actual_self
			actual_self = anterior_self.prox
		return le

class ListaDobleEnlazada:

	def __init__(self):
		self.prim = None
		self.ultimo = None

	def append(self, valor):
		nuevo = Nodo(valor)
		if self.prim == None:
			self.prim =	nuevo
			self.ultimo = nuevo
		else:
			anterior = self.prim
			actual = anterior.prox
			while actual is not None:
				anterior = actual
				actual = anterior.prox
			anterior.prox = nuevo
			self.ultimo = nuevo
	def pop(self):
		anterior = self.prim
		actual = anterior.prox
		siguiente = actual.prox
		while siguiente is not None:
			anterior = actual
			actual = anterior.prox
			siguiente = actual.prox
		anterior.prox = None
		self.ultimo = anterior

	def insert(self, indice, valor):
		nuevo = Nodo(valor)
		if indice == 0:
			self.prim = nuevo
			if self.prim.prox == None:
				self.ultimo = nuevo
		else:
			anterior = self.prim
			actual = anterior.prox
			for i in range(1, indice):
				anterior = actual
				actual = anterior.prox
			if actual.prox == None:
				actual.prox = nuevo
			else:
				nuevo.prox = actual
				anterior.prox = nuevo
	def remove(self, valor):
		if self.prim.dato == valor:
			self.prim = self.prim.prox
		else:
			anterior = self.prim
			actual = anterior.prox
			while actual.dato != valor:
				anterior = actual
				actual = anterior.prox
			anterior.prox = actual.prox		


l = ListaDobleEnlazada()

l.append(14)
l.append(1)
l.append(95)
l.append(124)
l.append(24)
l.append(3)
l.append(39)
l.append(3)
l.pop()
l.pop()
l.insert(4, 234)
l.remove(95)
nodo = l.prim
while nodo is not None:
	print(nodo.dato)
	nodo = nodo.prox




