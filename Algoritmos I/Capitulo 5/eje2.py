def fact_primos(num):
	x = 2
	while x <= num:
		if num % x == 0:
			print(x, end=" ")
			num = num / x
		x = x + 1
		
fact_primos(int(input("Ingresar un numero: ")))