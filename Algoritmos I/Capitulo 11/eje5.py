def rot13(origen, destino):
	with open(origen, "rb") as ori:
		with open(destino, "w") as dest:
			for linea in ori:
				print(linea)
				texto_bytes = ori.read(len(linea))
				for i in range(len(texto_bytes)):
					dest.write(str(i+13)%26)
rot13("tex.txt", "salida.txt")