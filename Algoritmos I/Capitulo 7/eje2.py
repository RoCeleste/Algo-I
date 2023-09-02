def encajan(t1, t2):

	return t1[0] in t2 or t1[1] in t2
print(encajan((3, 4), (5, 4)))

def encajan2(cad):
	fichas = cad.split(" ")
	return fichas[0][0] in fichas[1] or fichas[0][2] in fichas[1]

