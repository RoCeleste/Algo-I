# a)
def tiempo_a_segundos(horas, minutos, segundos):
	return horas * 3600 + minutos * 60 + segundos


# b)
def segundos_a_tiempo(total):
	horas = int((total - total % 3600) / 3600)
	total = total - (horas * 3600)
	minutos = int((total - total % 60) / 60)
	total = total - (minutos * 60)
	segundos = total
	return horas, minutos, segundos
