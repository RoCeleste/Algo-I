import random

num = random.randrange(1, 10)
correcto = False
while correcto == False:
	intento = int(input("Adivina el numero (entre 1 y 10): "))
	if intento > num:
		print("Muy alto")
	elif intento < num:
		print("Muy bajo")
	else:
		print("Correcto")
		correcto == True
		break	