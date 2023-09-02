import time

CONTRASEÑA = "mfpaez"
limite = 3
intentos = 0

while intentos != limite:
	entrada = input("Ingresar contraseña: ")
	if entrada != CONTRASEÑA:
		print("No es la contraseña correcta.")
		intentos = intentos + 1
		time.sleep(intentos)
	else:
		print("Contraseña correcta")
		break
if intentos == limite:

	print("superaste el numero de intentos")		