class Vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return f"[{self.x},{self.y},{self.z}]"

	def __repr__(self):
		return f"[{self.x}, {self.y}, {self.z}]"

	def __add__(self, otro):
		
		if len([int(i) for i in repr(otro) if i.isdigit()]) != 3:		# lista con numeros enteros extraidos de la cadena resultante de repr(otro)
			raise Exception("vectores con distinta longitud")
		else:
			return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

	def __mul__(self, escalar):
		return Vector(self.x * escalar, self.y * escalar, self.z * escalar)
