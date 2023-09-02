def digito_en_numero(dig, num):
	while num > 10:
		decimal = num % 10
		print(decimal)
		if decimal == dig:
			return True
		num = num // 10
	return False	

print(digito_en_numero(3,593242))		