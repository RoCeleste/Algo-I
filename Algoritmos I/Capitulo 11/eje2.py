def cp(origen, destino):
	with open(origen, "r") as ori:
		with open(destino, "w") as dest:
			for i in ori:
				dest.write(i)
				
