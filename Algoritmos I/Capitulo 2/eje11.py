n = int(input("1 hasta: "))

for x in range(1, n+1):
	for y in range(1, n+1):
		print("*" * x, "|", "*" * y)