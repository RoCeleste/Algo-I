def cargar_datos(archivo):
	dic = {}
	with open(archivo, "r") as f:
		for linea in f:
			linea = linea.strip()
			lista = linea.split(",")
			dic[lista[0]] = lista[1]
	return dic
def guardar_datos(diccionario, archivo):
	with open(archivo, "w") as dest:
		for i in diccionario:
			dest.write(f"{i}, {diccionario[i]}\n")
guardar_datos({"Wanda" : "Nara", "Leo" : "Messi"}, "xet.txt")