def producto_mayor(a,b,c,d):
	mayor = 0
	if max(a*b, a*c, a*d) > mayor:
		mayor = max(a*b, a*c, a*d)
	if max(b*a, b*c, b*d) > mayor:
		mayor = max(b*a, b*c, b*d)
	if max(c*a, c*b, c*d) > mayor:
		mayor = max(c*a, c*b, c*d)
	if max(d*a, d*b, d*c) > mayor:
		mayor = max(d*a, d*b, d*c)	
	return mayor

print(producto_mayor(1,15,-3,-4))	
