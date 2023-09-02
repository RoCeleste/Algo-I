def corrector(ej_totales, porcentaje):
	resueltos = int(input("Cantidad de ej. resueltos(-1 para salir): "))
	ej_para_aprobar = ej_totales * porcentaje / 100
	while resueltos != -1:
		if resueltos >= ej_para_aprobar:
			porcentaje_resueltos = resueltos * 100 / ej_totales
			print(porcentaje_resueltos,"% resuelto, aprobade")
		else:
			porcentaje_resueltos = resueltos * 100 / ej_totales
			print(porcentaje_resueltos,"% resuelto, aplazade")
		resueltos = int(input("Cantidad de ej. resueltos(-1 para salir): "))	

corrector(5,60)