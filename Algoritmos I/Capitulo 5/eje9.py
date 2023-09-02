def multiplos_menores(a,b):
	c=0
	for i in range(a,b):
		if (a*i) < b:
			
			c += 1
	return c

def multiplos_menores(a,b):
	i=2
	while i*a < b:
		i+=1
	return i		
print(multiplos_menores(24,954))

# la del for		