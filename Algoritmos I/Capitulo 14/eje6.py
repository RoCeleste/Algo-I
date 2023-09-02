class Caja:

	def __init__(self, diccionario):
		self.diccionario = diccionario

		for i in self.diccionario:
			if i not in [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]:
				raise ValueError(f"Denominacion {i} no permitida")
	def __str__(self):
		return f"Caja {self.diccionario} total: {sum([llave * self.diccionario[llave] for llave in self.diccionario])}"

	def agregar(self, diccionario):
		c = Caja(diccionario)
		for llave in c.diccionario:
			if llave in self.diccionario:
				self.diccionario[llave] += c.diccionario[llave]
			else:
				self.diccionario[llave] = 1	
		return self

	def quitar(self, diccionario):
		c = Caja(diccionario)
		for llave in c.diccionario:
			if llave in self.diccionario:
				if self.diccionario[llave] < c.diccionario[llave]:
					raise ValueError("no hay suficientes billetes de esa denominacion en caja")
				self.diccionario[llave] -= c.diccionario[llave]

			else:
				raise KeyError("no hay billetes de esa denominacion en caja")
		return self

