class Fraccion:
	def __init__(self, dividendo, divisor):
		self.dividendo = dividendo
		self.divisor = divisor

	def __str__(self):
		return f"{self.dividendo}/{self.divisor}"

	def __add__(self, otro):
		suma_divisor = self.divisor * otro.divisor
		suma_dividendo = otro.divisor * self.dividendo + self.divisor * otro.dividendo
		return Fraccion(suma_dividendo, suma_divisor)

	def __mul__(self, otro):
		return Fraccion(self.dividendo * otro.dividendo, self.divisor * otro.divisor)

	def simplificar(self):
		divisor = self.divisor
		dividendo = self.dividendo

		for i in range(1, int(self.divisor)):
			if int(self.dividendo / i) == self.dividendo / i and int(self.divisor / i) == self.divisor / i:

				divisor = int(self.divisor / i)
				dividendo = int(self.dividendo / i)
				
		return Fraccion(dividendo, divisor)

