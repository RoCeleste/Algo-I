import eje1

print("Ingresar tiempo 1")

horas1 = int(input("horas: "))
minutos1 = int(input("minutos: "))
segundos1 = int(input("segundos: "))

print("Ingresar tiempo 2")

horas2 = int(input("horas: "))
minutos2 = int(input("minutos: "))
segundos2 = int(input("segundos: "))

suma = eje1.tiempo_a_segundos(horas1, minutos1, segundos1) + eje1.tiempo_a_segundos(horas2, minutos2, segundos2)
hora_final, minuto_final, segundo_final = eje1.segundos_a_tiempo(suma)
print(hora_final,"h:",minuto_final,"m:",segundo_final,"s")