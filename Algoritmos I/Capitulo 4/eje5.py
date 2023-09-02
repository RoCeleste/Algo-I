# a)
def bisiesto(año):
	if año % 400 == 0:
		return "bisiesto"
	if año % 4 == 0 and not año % 100 == 0:
		return "bisiesto"
	else:
		return "no es bisiesto"
# b)

