class Materia:
	def __init__(self, codigo, nombre, creditos):
		self.codigo = codigo
		self.nombre = nombre
		self.creditos = creditos

		if not isinstance(self.codigo, str) or not isinstance(self.nombre, str) or not isinstance(self.creditos, int):
			raise Exception("codigo y nombre tienen que ser cadenas y horas, un numero entero")

class Carrera:
	def __init__(self, materias):
		self.materias = materias
		self.reporte = {"Creditos" : 0, "TotalNotas" : "N/A", "Aprobadas" : []}

	def __str__(self):
		return f"Creditos: {self.reporte["Creditos"]} -- Promedio: {self.reporte["TotalNotas"] / len(self.reporte["Aprobadas"])} -- Materias Aprobadas: {self.reporte["Aprobadas"]}"

	def aprobar(self, codigo, nota):
		for materia in self.materias:
			if materia.codigo == codigo:
				self.reporte["Creditos"] += materia.creditos
				self.reporte["Aprobadas"].append(f"{materia.codigo} {materia.nombre} ({nota})")
				self.reporte["TotalNotas"] += nota
				return
		raise ValueError("Esa materia no esta en el plan de carrera")
anmat = Materia("61.03", "AMII", 8)
alge = Materia("61.01", "Algebra II", 8)
algo = Materia("72.02", "Algo I", 6)
c = Carrera([anmat, algo, alge])
print(c)		