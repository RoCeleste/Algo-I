def bin_a_dec(cad_bin):
	total = 0
	cont = 0
	for i in cad_bin[::-1]:
		print(i)
		cont += 1
		total += int(i)*(2**cont)
	return total
print(bin_a_dec("01011101"))