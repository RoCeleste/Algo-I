def primos_acotados(m):
	c=0
	for i in range(1,m):
		for j in range(2, i):
			if i % j == 0:
				break
			if j == i-1:
				c+=1
				print(i)


	return c+2		
print(primos_acotados(100))