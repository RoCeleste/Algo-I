#terminar
class Intervalo:

	def  __init__(self, desde, hasta):
		if isinstance(desde, int) and isinstance(hasta, int) and desde < hasta:
			self.desde = desde
			self.hasta = hasta
		else:
			raise Exception("desde y hasta tienen que ser numeros enteros y desde < hasta")

	def duracion(self):
		return self.hasta - self.desde

	def interseccion(self, otro):
		if self.desde > otro.hasta or self.hasta < otro.desde:
			raise Exception("no hay interseccion")
		else:
			menor_sup = self.hasta if self.hasta < otro.hasta else otro.hasta
			mayor_inf = self.desde if self.desde > otro.desde else otro.desde

			return Intervalo(mayor_inf, menor_sup)
		
	def union(self, otro):
		if self.hasta < otro.desde or self.desde > otro.hasta:
			raise Exception("no son adyacentes ni se intersecan")
		else:
			menor_inf = self.desde if self.desde < otro.desde else otro.desde
			mayor_sup = self.hasta if self.hasta > otro.hasta else otro.hasta

			return Intervalo(menor_inf, mayor_sup)


