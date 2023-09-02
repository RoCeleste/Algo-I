num = int(input("Numeros triangulares hasta: "))

total = 0
for x in range(1, num+1):
	total = total + x
	print(x, "-", total)