# a)
def paridad(num):
	if num % 2 == 0:
		return "par"
	else:
		return "impar"

# b)
def primo(num):
	if num == 2:
		return "primo"
	if num % 2 == 0:
		return "multiplo"
	for x in range(3, int(num / 2), 2):
		if num % x == 0:
			return "multiplo"
	return "primo"


