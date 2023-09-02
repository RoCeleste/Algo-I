def palabra_mas_larga(texto):
	dic = {}
	texto = texto.lower()
	palabras = texto.split()
	for caracter in texto:
		max_longitud = 0
		max_palabra = palabras[0]
		if not caracter.isalpha():
			continue
		for palabra in palabras:
			if not caracter in palabra:
				continue
			if len(palabra) > max_longitud:
				max_longitud = len(palabra)
				max_palabra = palabra
		dic[caracter] = max_palabra		
	return dic			
