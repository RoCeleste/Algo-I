class TorreDeControl:
	def __init__(self):
		self.aterrizando = []
		self.despegando = []
		self.cola = []

	def nuevo_arribo(self, avion):
		self.aterrizando.append(avion)
		self.cola.append(avion)

	def nueva_partida(self, avion):
	
		self.despegando.append(avion)
		self.cola.append(avion)
	def ver_estado(self):
		cadena = ""
		for avion in self.aterrizando:
			cadena += avion + ", "
		cadena2 = ""
		for avion in self.despegando:
			cadena2 += avion + ", "
		print(f"Esperando para aterrizar: {cadena}")
		print(f"Esperando para despegar: {cadena2}")

	def asignar_pista(self):
		if len(self.aterrizando) > 0:
			avion = self.aterrizando.pop(0)
			print(f"Aterrizo {avion}")
		elif len(self.despegando) > 0:
			avion = self.despegando.pop(0)
			print(f"Despego {avion}")
		else:
			raise IndexError("La cola esta vacia")
torre = TorreDeControl()
torre.nuevo_arribo("24")
torre.nueva_partida("53")
torre.ver_estado()
torre.nueva_partida("983")
torre.asignar_pista()
torre.asignar_pista()
